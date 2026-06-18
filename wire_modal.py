#!/usr/bin/env python3
# Update the modal wiring

with open('dripluxedetailing.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Change the "Schedule a Detail" button to trigger the modal
old_button = '''          <button class="btn btn-primary" data-page="booking">Schedule a Detail</button>'''
new_button = '''          <button class="btn btn-primary" id="confirm-booking">Schedule a Detail</button>'''

content = content.replace(old_button, new_button)

# Update the button event listener setup to handle modal triggers better
old_listeners = '''    document.getElementById('confirm-booking').addEventListener('click', openModal);
    document.getElementById('modal-close').addEventListener('click', closeModal);
    document.getElementById('success-close').addEventListener('click', closeModal);'''

new_listeners = '''    document.getElementById('confirm-booking').addEventListener('click', openModal);
    document.getElementById('modal-close').addEventListener('click', closeModal);
    document.getElementById('success-close').addEventListener('click', closeModal);
    document.getElementById('form-cancel').addEventListener('click', closeModal);'''

content = content.replace(old_listeners, new_listeners)

# Fix the package-selection click handler
old_pkg_handler = '''    document.querySelectorAll('#package-selection').addEventListener('click', function(e) { if (e.target.classList.contains('btn') && e.target.dataset.pkg) selectPackageStep(e.target); });'''
new_pkg_handler = '''    document.getElementById('packages-modal').addEventListener('click', function(e) { if (e.target.classList.contains('btn') && e.target.dataset.pkg) selectPackageStep(e.target); });'''

content = content.replace(old_pkg_handler, new_pkg_handler)

with open('dripluxedetailing.html', 'w', encoding='utf-8') as f:
    f.write(content)
    
print("✓ Modal wiring updated")
