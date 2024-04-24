from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from flask import jsonify

from flaskr.db import get_db

bp = Blueprint('blog', __name__)

@bp.route('/')
def index():
    db = get_db()
    cursor = db.cursor()

    # Execute SQL query to fetch posts
    cursor.execute(
        'SELECT id, title, body, created'
        ' FROM blog'
        ' ORDER BY created DESC'
    )

    # Fetch all rows from the cursor
    blogs = cursor.fetchall()

    # Convert posts to a list of dictionaries
    blog_list = []
    for blog in blogs:
        blog_dict = {
            'id': blog[0],
            'title': blog[1],
            'body': blog[2],
            'created': blog[3]
        }
        blog_list.append(blog_dict)

    # Close the cursor and database connection
    cursor.close()
    db.close()

    # Return posts in JSON format
    return jsonify(blogs=blog_list)

@bp.route('/create', methods=['POST'])
def create():
    title = request.form.get('title')
    body = request.form.get('body')

    error = None

    if not title:
        error = 'Title is required.'

    if error is not None:
        flash(error)
    else:
        db = get_db()
        cursor = db.cursor()
        try:
            cursor.execute(
                'INSERT INTO blog (title, body) VALUES (%s, %s)',
                (title, body)
            )
            db.commit()
        except Exception as e:
            db.rollback()
            flash('An error occurred while creating the post.')
        finally:
            cursor.close()
            db.close()
        return redirect(url_for('blog.index'))