# What happens when you type *https://www.google.com* in your browser and press ```Enter```? 

1. As soon as we enter the web address name (www.google.com) in our browser (chrome) and press enter the browser will send this web address name i.e (Domain name) to the ISP asking for the IP address of the webpage.

2. The ISP in turn sends a request to a DNS (Domain Name Server) asking for the IP address. The DNS will search its records for the IP address mapped with the webpage and will return that to the ISP which would then reply the browser with the IP address of the webpage. 

3. The browser would dial in the IP address and then create a secure https/ssl tunnel with the particular website that the IP address points to before directly sending a http get request from your system to that IP address through your ISP.

4. When the request gets to the dialed IP address, a firewall first has to process the request to confirm that it is not a malicious request that could be trying to attack the website's infrastructure. 

5. If the firewall finds no signals that it is a malicious request, the http request is allowed to go through to the load balancer. The load balancer, forwards the request to the next available application server based on whichever load balancing algorithm it has been configured with. 

5. The application server then processes the http request based on the headers and information encapsulated in it and queries the database to generate a dynamic webpage consisting of html, css and Javascript files. 

6. The application server now passes the dynamically generated webpage to web server which would then send an http response containing the html, css and javascript files that makes up the Google webpage back to your computer. 

5. Once the browser on your computer receives this http response, it parses the headers and body content of the http response from the Google servers and renders the Google website on the screen using the html, css and javascript information gotten from the response of the web server.
