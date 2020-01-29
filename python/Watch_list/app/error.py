from flask import Flask
from app import app

@app.errorhandler(404)
def four_Ow_four(error):
    '''
    Function to render the 404 page
    '''
    return render_template(fourOwfour.html),404
    