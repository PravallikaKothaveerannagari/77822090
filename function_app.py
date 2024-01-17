import azure.functions as func
from flask import Flask, request, Response, redirect, url_for
from wsgi import app
app = func.WsgiFunctionApp(app=app.wsgi_app, http_auth_level=func.AuthLevel.ANONYMOUS)

