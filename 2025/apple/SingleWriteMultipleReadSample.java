// single write, multiple read sudo
// using two locks to avoid starvation
public class SingleWriteMultipleReadSample {
    Object statLock = null;
    Object queueLock = null;
    Queue<Integer> queue = null;
    int readCount = 0;
    boolean isWriting = false;

    public SingleWriteMultipleReadSample() {
        statLock = new Object();
        queueLock = new Object();
        queue = new LinkedList<>();

    }

    public void enqueue(int value) {
        synchronized(statLock) {
            while (isWriting || readCount > 0) {
                statLock.wait();
            }
            isWriting = true;
        }
        synchronized(queueLock) {
            queue.add(value);
        }
        synchronized(statLock) {
            isWriting = false;
            statLock.notifyAll();
        }

    
    }

    public int dequeue() {
        synchronized(statLock) {
            while (queue.isEmpty() || isWriting || readCount > 0) {
                statLock.wait();
            }
            isWriting = true;
        }
        int val;
        synchronized(queueLock) {
            val = queue.poll();
        }
        synchronized(statLock) {
            isWriting = false;
            statLock.notifyAll();
        }
        return val;
    }

    public int read() {

        synchronized(statLock) {
            while (isWriting || readCount >= 10 || queue.isEmpty()) {
                statLock.wait();
            }
            readCount++;
        }
        int val;
        synchronized(queueLock) {
            val = queue.peek();
        }
        synchronized(statLock) {
            readCount--;
            statLock.notifyAll();
        }
        return val;
    }
}
