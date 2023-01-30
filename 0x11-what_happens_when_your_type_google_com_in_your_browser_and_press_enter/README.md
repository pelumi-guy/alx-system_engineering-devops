This is a very layman description of what happens in the back end. I tried not to use any big technical jargons.

1. As soon as we enter the web address name(Google) in our browser (chrome) and press enter the browser will send this web address name i.e(Domain name) to the ISP(internet service provider like airtel , hatway etc) asking for the IP address of the webpage.

2. Since ISP doesnt have the IP address it will in turn send a request to DNS(Domain Name Server) asking for the IP address. DNS will search for the IP address mapped with the webpage and will return that to the ISP who in turn will return it to the browser.

3. Browser now will dial in the IP address of the particular website and this will directly send request from your system to web page server(google server) through your ISP where the google server will send you back the required information to display on your browser.


When a pc boots up it obtains its own IP address, IP address of DNS server and Default gateway and subnet block using DHCP (Dynamic Host Control Protocol).
To send DNS query for name-to-IP address translation of requested web page, it requires MAC address of Default router, and for this it uses Address Resolution Protocol (ARP) and obtains physical Address of the default gateway router.
Then sends DNS query to the DNS server, which replies back with DNS response with the IP address of requested web page, that is cached into the forwarding table.
Now the client creates a TCP socket to interact with the web server and sends a tcp sync message. Server replies back with tcp sync ack message.
Now we can move ahead with HTTP get message, and the server will respond back with HTTP response.
It is an elaborate process which covers most of the network related topics. For detailed explanation of the above and for step by step procedure you can visit my blog A Day in the Life of Web-Page Request. I hope it will provide you with better clarity and understanding of what goes in.
