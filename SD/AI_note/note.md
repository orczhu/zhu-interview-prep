### Good Doc ###
https://levelup.gitconnected.com/building-an-advanced-agentic-rag-pipeline-that-mimics-a-human-thought-process-687e1fd79f61#14fe

SAML vs Oauth

SAML is more using by user sign in
user -> IDP
IDP auth user, passcode/MFA
create SAML assertation signed by IDP private key and append cert (public key) in SAML assertion.
IDP - SP (SP verify signature by public key and extract wanted info from attributes)

