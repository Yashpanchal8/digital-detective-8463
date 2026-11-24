# Mission 7 — How computers communicate

## 1. Task / objective
Explain network types and concepts, check connectivity and DNS, and describe how a browser opens a website.

## 2. Work completed
### 7.1 Network concepts
| Concept | Explanation | Common use |
|---|---|---|
| LAN | Connects devices across a small area. | Home or classroom network |
| MAN | Covers a city or large campus. | City-wide public network |
| WAN | Connects networks over large distances. | The Internet |
| DNS | Finds network addresses associated with domain names. | Looking up `example.com` |
| Router | Forwards traffic between networks. | Sends home traffic toward an ISP |
| Protocol | Rules devices follow to communicate. | HTTPS |
| Packet switching | Splits data into packets that travel across networks. | Web traffic carried by IP packets |
| Client-server | A client requests a service and a server responds. | Browser requesting a page |

### 7.2 Network observations
I ran `nslookup example.com`; it returned `104.20.23.154` and `172.66.147.243` at the time of the lookup. I also ran `ping -c 4 example.com`; all four packets received replies, with 0% packet loss. DNS addresses can change. I did not include local resolver or network details.

A connectivity check helps determine whether a destination responds and how long replies take. A DNS lookup asks a resolver for addresses associated with a domain name. When the lookup succeeds, the browser can use an address to contact the server.

### 7.3 Opening a website
1. I enter a web address in the browser; the browser is the client.
2. DNS looks up the domain name and returns an address.
3. The device sends packets through its router and other networks.
4. The client and server establish a connection using network protocols.
5. The browser sends an HTTP request, normally protected by HTTPS.
6. The server returns the requested page and related resources.
7. The browser processes the response and displays the page.

## 3. Commands / tools used
`ping -c 4 example.com` checks connectivity; `nslookup example.com` looks up DNS records.

## 4. My understanding
DNS translates a human-readable name into an address that computers can use. A router forwards packets, and protocols define how a client and server exchange requests and responses.

## 5. Difficulties faced
The first attempt ran in a restricted shell and could not resolve the domain.

## 6. How I resolved them
I reran the read-only commands with network access and recorded only the public domain results. Any private IP address or Wi-Fi information should be redacted.

## 7. Evidence / files
This README contains the concepts table, the recorded command result and a seven-step website explanation.

## 8. Commit details
- Commit message: `Explain networking concepts and website communication`.
- The mission commit is pushed to GitHub.
