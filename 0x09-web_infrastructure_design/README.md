## 0x09. Web infrastructure design

## Description
- This project involves designing and documenting various web infrastructures for hosting the website www.foobar.com. Each task requires creating diagrams and explanations for different configurations, considering factors like scalability, reliability, security, and monitoring.

## Tasks

- Simple Web Stack

Design a single-server web infrastructure using a LAMP stack.
Requirements include a server, Nginx web server, application server, MySQL database, and domain name configuration for www.foobar.com.
Issues with the infrastructure include single points of failure, downtime during maintenance, and scalability limitations.

- Distributed Web Infrastructure

Design a three-server web infrastructure with load balancing using HAproxy.
Requirements include two servers, Nginx web server, application server, HAproxy load balancer, MySQL database, and distribution algorithm explanation.
Issues include single points of failure, security concerns, and lack of monitoring.

- Secured and Monitored Web Infrastructure

Design a three-server web infrastructure with security measures and monitoring.
Requirements include firewalls, SSL certificate for HTTPS, monitoring clients, and explanation of security and monitoring purposes.
Issues include SSL termination at the load balancer, single MySQL server for writes, and identical server components leading to potential problems.
