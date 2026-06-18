#!/usr/bin/env python3
# Update the booking modal to support new multi-step flow

# Read the file
with open('dripluxedetailing.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the entire modal
old_modal_start = '<div class="modal-overlay" id="booking-modal">'
old_modal_end = '</div>\n  </main>'

# Find the modal section
start_idx = content.find(old_modal_start)
end_idx = content.find(old_modal_end, start_idx)

if start_idx != -1 and end_idx != -1:
    # Extract everything before modal
    before = content[:start_idx]
    # Extract everything after modal
    after = content[end_idx:]
    
    # New modal HTML
    new_modal = '''<div class="modal-overlay" id="booking-modal">
      <div class="modal">
        <div class="modal-header">
          <div>
            <h2 class="modal-title" id="modal-title-text">Select Your Service</h2>
            <p class="modal-subtitle" id="modal-subtitle-text">Choose the detailing service you'd like to book.</p>
          </div>
          <button id="modal-close" aria-label="Close">×</button>
        </div>
        <div id="service-selection" style="display: block;">
          <div class="form-actions" style="flex-direction: column; gap: 1rem;">
            <button type="button" class="btn btn-secondary" style="text-align: left;" data-service="interior">Interior Detailing</button>
            <button type="button" class="btn btn-secondary" style="text-align: left;" data-service="exterior">Exterior Detailing</button>
            <button type="button" class="btn btn-secondary" style="text-align: left;" data-service="full">Full Detail</button>
          </div>
        </div>
        <div id="package-selection" style="display: none;">
          <div class="form-actions" style="flex-direction: column; gap: 1rem;" id="packages-modal"></div>
          <div class="form-actions" style="margin-top: 1.5rem;">
            <button type="button" class="btn btn-secondary" id="back-to-service">← Back</button>
          </div>
        </div>
        <form id="booking-form" style="display: none;">
          <div class="booking-summary" id="modal-summary"></div>
          <div class="form-grid">
            <div style="grid-column: 1 / -1;">
              <label class="form-label" for="modal-name">Full Name</label>
              <input id="modal-name" class="form-input" type="text" placeholder="Your Name" required />
              <div class="form-error" id="error-modal-name">Please enter your name</div>
            </div>
            <div style="grid-column: 1 / -1;">
              <label class="form-label" for="modal-phone">Phone</label>
              <input id="modal-phone" class="form-input" type="tel" placeholder="(555) 123-4567" required />
              <div class="form-error" id="error-modal-phone">Please enter your phone number</div>
            </div>
            <div>
              <label class="form-label" for="modal-date">Date</label>
              <input id="modal-date" class="form-input" type="date" required />
              <div class="form-error" id="error-modal-date">Please select a date</div>
            </div>
            <div>
              <label class="form-label" for="modal-time">Time</label>
              <input id="modal-time" class="form-input" type="time" min="09:00" max="18:00" required />
              <div class="form-error" id="error-modal-time">Please select a time</div>
            </div>
          </div>
          <div class="form-actions">
            <button type="button" class="btn btn-secondary" id="back-to-package">← Back</button>
            <button type="button" class="btn btn-primary" id="confirm-details">Next: Send Booking</button>
          </div>
        </form>
        <div id="send-choice" style="display: none;">
          <p style="color: rgba(232,237,248,0.8); margin-bottom: 1.5rem;">Choose how you want to send your booking request:</p>
          <div class="form-actions" style="flex-direction: column; gap: 1rem;">
            <button type="button" class="btn btn-primary" id="send-whatsapp" style="justify-content: center;">Send via WhatsApp</button>
            <button type="button" class="btn btn-secondary" id="send-sms" style="justify-content: center;">Send via SMS</button>
            <button type="button" class="btn btn-secondary" id="back-to-details" style="justify-content: center;">← Back</button>
          </div>
        </div>
        <div class="success-state" id="success-state">
          <div class="success-card">
            <h3 class="success-title">Booking Request Sent!</h3>
            <p class="success-text">Your booking details have been sent successfully. We'll confirm your appointment shortly.</p>
            <div class="form-actions"><button type="button" class="btn btn-primary" id="success-close" style="justify-content: center; width: 100%;">Done</button></div>
          </div>
        </div>
      </div>
    </div>'''
    
    # Reconstruct content
    new_content = before + new_modal + after
    
    # Write back
    with open('dripluxedetailing.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("✓ Modal updated successfully")
else:
    print("✗ Could not find modal structure")
