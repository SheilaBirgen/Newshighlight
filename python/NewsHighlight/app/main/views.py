from flask import render_template,request,url_for,redirect
from . import main
from ..requests import get_movies,get_movie,search_movie
from .forms import ReviewForm