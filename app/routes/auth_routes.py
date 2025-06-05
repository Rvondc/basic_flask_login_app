from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.services.auth_service import AuthService


bp = Blueprint('auth', __name__)
auth_service = AuthService()

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if 'user_id' in session: # Using Flask sessions directly
        return redirect(url_for('auth.dashboard'))

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if auth_service.verify_credentials(username, password):
            session['user_id'] = username
            flash('Login successful!', 'success')

            return redirect(url_for('auth.dashboard'))
        else:
            flash('Invalid username or password.', 'danger')
    return render_template('login.html', title='Login')

@bp.route('/dashboard')
def dashboard():
    if 'user_id' not in session: # Check for Flask session
         flash('Please log in to access this page.', 'warning')
         return redirect(url_for('auth.login'))

    # username = current_user.id
    username = session.get('user_id') # Flask session
    return render_template('dashboard.html', title='Dashboard', username=username)

@bp.route('/logout')
def logout():
    session.pop('user_id', None) # Clear Flask session
    flash('You have been logged out.', 'info')
    return redirect(url_for('auth.login'))