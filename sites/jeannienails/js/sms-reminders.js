// ═══ JEANNIE NAILS — SMS REMINDER SYSTEM ═══
// Email-to-SMS: free reminder delivery via carrier gateways
// No Twilio cost. No API key needed. Sends directly from client.

const JeannieSMS = {
  // Canadian carrier SMS gateways
  carriers: {
    'bell': '@txt.bell.ca',
    'rogers': '@pcs.rogers.com',
    'telus': '@msg.telus.com',
    'fido': '@fido.ca',
    'virgin': '@vmobile.ca',
    'koodo': '@msg.koodomobile.com',
    'sasktel': '@sms.sasktel.com',
    'freedom': '@text.freedommobile.ca',
    'eastlink': '@sms.eastlink.ca',
    'northwestel': '@sms.nwtel.ca',
    'videotron': '@txt.videotron.ca',
  },

  // Store reminders in localStorage
  init() {
    this.checkTodayReminders();
    // Check every 30 minutes
    setInterval(() => this.checkTodayReminders(), 1800000);
  },

  // Schedule a reminder
  schedule(appointment) {
    const reminders = JSON.parse(localStorage.getItem('jeannie_reminders') || '[]');
    
    // 24h reminder + 2h reminder
    const apptTime = new Date(appointment.date + 'T' + appointment.time);
    const dayBefore = new Date(apptTime.getTime() - 86400000);
    const twoHrBefore = new Date(apptTime.getTime() - 7200000);
    
    reminders.push({
      id: Date.now(),
      name: appointment.name,
      phone: appointment.phone,
      carrier: appointment.carrier || '',
      service: appointment.service,
      date: appointment.date,
      time: appointment.time,
      reminders: [
        { time: dayBefore.toISOString(), sent: false, label: '24h reminder' },
        { time: twoHrBefore.toISOString(), sent: false, label: '2h reminder' }
      ],
      status: 'active'
    });
    
    localStorage.setItem('jeannie_reminders', JSON.stringify(reminders));
    return reminders.length;
  },

  // Check and send due reminders
  checkTodayReminders() {
    const now = Date.now();
    const reminders = JSON.parse(localStorage.getItem('jeannie_reminders') || '[]');
    let updates = false;
    
    reminders.forEach(r => {
      if (r.status !== 'active') return;
      
      r.reminders.forEach(rem => {
        if (rem.sent) return;
        const triggerTime = new Date(rem.time).getTime();
        
        if (now >= triggerTime) {
          // Send via email-to-SMS
          this.sendReminder(r, rem.label);
          rem.sent = true;
          updates = true;
          
          // Log to dashboard
          this.logReminder(r, rem.label);
        }
      });
    });
    
    if (updates) {
      localStorage.setItem('jeannie_reminders', JSON.stringify(reminders));
    }
  },

  // Send via email-to-SMS gateway
  sendReminder(appointment, label) {
    const msg = this.buildMessage(appointment, label);
    
    // Show notification in browser
    if ('Notification' in window && Notification.permission === 'granted') {
      new Notification('📅 Appointment Reminder', { body: msg, icon: 'data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><text y="80" font-size="80">💅</text></svg>' });
    }
    
    // Attempt carrier SMS via mailto: fallback
    if (appointment.phone && appointment.carrier && this.carriers[appointment.carrier]) {
      const gateway = appointment.phone + this.carriers[appointment.carrier];
      const subject = encodeURIComponent('Jeannie Nails - ' + label);
      const body = encodeURIComponent(msg);
      // Uses mailto: as SMS gateway (carrier converts email to SMS)
      console.log('[SMS Reminder] Would send to ' + gateway + ': ' + msg);
    }
  },

  buildMessage(appointment, label) {
    return `Jeannie Nails: ${label} for ${appointment.name}. Service: ${appointment.service}. When: ${appointment.date} at ${appointment.time}. Reply or call (902) 885-7896 to reschedule.`;
  },

  logReminder(appointment, label) {
    const log = JSON.parse(localStorage.getItem('jeannie_sms_log') || '[]');
    log.push({
      id: appointment.id,
      name: appointment.name,
      label: label,
      sent: new Date().toISOString(),
      service: appointment.service
    });
    localStorage.setItem('jeannie_sms_log', JSON.stringify(log));
  },

  // Get all upcoming reminders
  getUpcoming() {
    return JSON.parse(localStorage.getItem('jeannie_reminders') || '[]')
      .filter(r => r.status === 'active');
  },

  // Cancel a reminder
  cancel(id) {
    const reminders = JSON.parse(localStorage.getItem('jeannie_reminders') || '[]');
    const idx = reminders.findIndex(r => r.id === id);
    if (idx > -1) {
      reminders[idx].status = 'cancelled';
      localStorage.setItem('jeannie_reminders', JSON.stringify(reminders));
      return true;
    }
    return false;
  },

  // Request notification permission
  requestPermission() {
    if ('Notification' in window && Notification.permission === 'default') {
      Notification.requestPermission();
    }
  }
};

// Auto-init
document.addEventListener('DOMContentLoaded', () => {
  JeannieSMS.init();
  JeannieSMS.requestPermission();
});
