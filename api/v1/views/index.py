#!/usr/bin/python3
"""index.py to connect to API"""
from api.vi.views import app_views
from flask import Flask, Blueprint, jsonify


@app_views.route('/status', strict_slashes=False)
def hbnbStatuse():
    """hbnbStatus"""
    return jsonify({"status": "ok"})
