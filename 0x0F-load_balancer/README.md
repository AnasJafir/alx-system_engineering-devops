Load Balancer

When a client types your domain name into their browser, the DNS resolves the domain name to the IP address of your load balancer. The client's browser then sends an HTTP request to your load balancer.

Here's the flow:

Client's Browser → Load Balancer:

The client's browser sends an HTTP request to your load balancer because it resolved your domain name to the load balancer's IP address.
The load balancer's frontend configuration specifies how to handle incoming requests. In this case, it listens on port 80 for HTTP requests (*:80) and forwards them to the backend defined as webnush_backend.
Load Balancer → Backend Servers:

The load balancer receives the HTTP request and forwards it to one of the backend servers (server1 or server2) based on the configured load-balancing algorithm (e.g., round-robin).
The backend server processes the request and generates an HTTP response.
Backend Servers → Load Balancer:

Once the backend server processes the request and generates a response, it sends the response back to the load balancer.
Load Balancer → Client's Browser:

The load balancer receives the response from the backend server and forwards it back to the client's browser.
The client's browser then renders the response and displays the webpage to the user.
In summary, the load balancer acts as a traffic distribution point, receiving incoming requests from clients and forwarding them to one of the backend servers. It then sends the responses from the backend servers back to the clients. This setup helps distribute the load evenly across multiple servers and ensures high availability and scalability for your web application.
