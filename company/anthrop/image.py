import os
import json

from PIL import Image, ImageFilter
from concurrent.futures import ProcessPoolExecutor

class ImageProcess:

    BASE = os.path.dirname(os.path.abspath(__file__))

    def load_images(self, directory):
        exts = ('.png', '.jpg', '.jpeg')
        images_path = []
        for f in sorted(os.listdir(directory)):
            if f.lower().endswith(exts):
                images_path.append(os.path.join(directory, f))
        return images_path

    def load_pipeline(self):
        directory = os.path.join(self.BASE, "transformation")
        pipeline = []
        for f in sorted(os.listdir(directory)):
            if f.lower().endswith('json'):
                with open(os.path.join(directory, f), 'r') as fh:
                    data = json.load(fh)
                pipeline.append((f, data['transformations']))
        return pipeline

    def apply_transform(self, images_path, pipelines):
        try:
            for image in images_path:
                image_memory = Image.open(image)
                image_name = os.path.splitext(image)[0]
                ext = os.path.splitext(image)[1]
                # for each image go through pipeline
                for f, pipeline in pipelines:
                    new_image = self.process(image_memory, pipeline)
                    transformed_name = os.path.splitext(f)[0]
                    # output to output folder
                    output_folder = os.path.join(self.BASE, 'output')
                    new_image.save(f'{output_folder}/{os.path.splitext(os.path.basename(image_name))[0]}__{transformed_name}{ext}')
        except Exception as e:
            print(e)



    def process(self, image_memory, pipeline):
            for op in pipeline:
                t = op['type']
                if t == 'grayscale':
                    image_memory = image_memory.convert('L')
                elif t == 'flip_horizontal':
                    image_memory = image_memory.transpose(Image.FLIP_LEFT_RIGHT)
                elif t == 'flip_vertical':
                    image_memory = image_memory.transpose(Image.FLIP_TOP_BOTTOM)
                elif t == 'scale':
                    factor = op['factor']
                    image_memory = image_memory.resize((int(image_memory.width * factor), int(image_memory.height * factor)))
                elif t == 'blur':
                    image_memory = image_memory.filter(ImageFilter.GaussianBlur(op['radius']))
                elif t == 'rotate':
                    image_memory = image_memory.rotate(op['angle'], expand=True)
                else:
                    raise ValueError(f'invalid op {t}')
            return image_memory

    def process_each(self, image_path, pipeline, f):
        image_memory = Image.open(image_path)
        new_image = self.process(image_memory, pipeline)
        image_name = os.path.splitext(os.path.basename(image_path))[0]
        ext = os.path.splitext(image_path)[1]

        new_image.save(f'{os.path.join(self.BASE, 'output')}/{image_name}_{f}{ext}')


    def run_parallel(self):
        with ProcessPoolExecutor(max_workers=os.cpu_count() - 1) as executor:
            for image_path in self.load_images(os.path.join(self.BASE, 'large_image')):
                for f, pipeline in self.load_pipeline():
                    executor.submit(self.process_each, image_path, pipeline, f)



if __name__ == '__main__':
    image_process = ImageProcess()
    # image_process.apply_transform(image_process.load_images(os.path.join(ImageProcess.BASE, 'small_image')), image_process.load_pipeline())
    # print("done")
    image_process.run_parallel()
    print("done")



# Be familar with folder op
# Pillow api
# Mutliprocess - ProcessPoolExecutor vs ThreadPoolExecutor