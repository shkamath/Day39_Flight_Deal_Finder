# Day39_Flight_Deal_Finder

The app will access(read/write) a remote google sheet document using the Sheety API and use the Tequila flight search API to find flight deals below a certain price threshold set by the user in the Google sheet. The scan will run every day on all cities listed in the document and if it finds a good deal, the user will be notified using the Twilio SMS service
