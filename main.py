from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from apis.general_pages.route_homepage import general_pages_router

def include_router(app):
	app.include_router(general_pages_router)

def configure_static(app):  #new
    app.mount("/static", StaticFiles(directory="static"), name="static")



def start_application():
	app = FastAPI()
	include_router(app)
	configure_static(app)
	return app


app = start_application()


#app = FastAPI()

#@app.get('/')
#def hello_api():
#    return {'Message':'Hello World!'}
