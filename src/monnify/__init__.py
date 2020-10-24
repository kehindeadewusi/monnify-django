#init.

mode = 'Production' # Or Test if you're still in test mode.
api_key = None
client_id = None
api_base = {
    'Production': 'https://sandbox.monnify.com/api/v2/',
    'Test': 'https://sandbox.monnify.com/api/v2/'
}
api_version = 'v2'
proxy = None
log = None
app_info = None #holds our default configurations, sent with new requests.

def set_info(name, mode, version):
    global app_info
    app_info = {
        "name": name,
        "mode": mode,
        "version": version
    }
