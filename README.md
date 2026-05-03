# 🌐 Static Routing Network — Cisco Packet Tracer

> A multi-router static routing implementation connecting 
> three LAN segments via serial WAN links.

![Cisco Packet Tracer](https://img.shields.io/badge/Cisco-Packet%20Tracer-blue)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![License](https://img.shields.io/badge/License-MIT-yellow)


## 📑 Table of Contents
- [Overview](#overview)
- [Network Topology](#network-topology)
- [IP Addressing Table](#ip-addressing-table)
- [Router Configurations](#router-configurations)
- [Static Routes Explained](#static-routes-explained)
- [Testing & Verification](#testing--verification)
- [How to Run](#how-to-run)
- [Key Learnings](#key-learnings)



## 📌 Overview
This project demonstrates static routing across a 3-router 
topology in Cisco Packet Tracer. Each router manages a unique 
LAN segment, and all inter-network communication is achieved 
through manually configured static routes — no dynamic 
routing protocols used.


## 🗺️ Network Topology

![Topology](screenshots/topology.png)

### Devices Used:
| Device    | Model       | Role              |
|-----------|-------------|-------------------|
| Router0   | Cisco 2621XM | Left Gateway     |
| Router1   | Cisco 2621XM | Central Hub      |
| Router2   | Cisco 2621XM | Right Gateway    |
| Switch0   | Cisco 2950   | LAN Switch (Left)|
| Switch1   | Cisco 2950   | LAN Switch (Mid) |
| Switch2   | Cisco 2950   | LAN Switch (Right)|
| PC0–PC5   | PC-PT        | End Hosts        |



## 📊 IP Addressing Table

| Device   | Interface | IP Address      | Subnet Mask       | Network         |
|----------|-----------|-----------------|-------------------|-----------------|
| Router0  | Se0/0     | 10.0.0.1        | 255.255.255.252   | 10.0.0.0/30     |
| Router0  | Fa0/0     | 192.168.10.1    | 255.255.255.0     | 192.168.10.0/24 |
| Router1  | Se0/0     | 10.0.0.2        | 255.255.255.252   | 10.0.0.0/30     |
| Router1  | Se0/1     | 11.0.0.1        | 255.255.255.252   | 11.0.0.0/30     |
| Router1  | Fa0/0     | 192.168.20.1    | 255.255.255.0     | 192.168.20.0/24 |
| Router2  | Se0/1     | 11.0.0.2        | 255.255.255.252   | 11.0.0.0/30     |
| Router2  | Fa0/0     | 192.168.30.1    | 255.255.255.0     | 192.168.30.0/24 |
| Switch0  | VLAN1     | 192.168.10.10   | 255.255.255.0     | 192.168.10.0/24 |
| Switch1  | VLAN1     | 192.168.20.20   | 255.255.255.0     | 192.168.20.0/24 |
| Switch2  | VLAN1     | 192.168.30.30   | 255.255.255.0     | 192.168.30.0/24 |
| PC0      | Fa0       | 192.168.10.2    | 255.255.255.0     | 192.168.10.0/24 |
| PC1      | Fa0       | 192.168.10.3    | 255.255.255.0     | 192.168.10.0/24 |
| PC2      | Fa0       | 192.168.20.2    | 255.255.255.0     | 192.168.20.0/24 |
| PC3      | Fa0       | 192.168.20.3    | 255.255.255.0     | 192.168.20.0/24 |
| PC4      | Fa0       | 192.168.30.2    | 255.255.255.0     | 192.168.30.0/24 |
| PC5      | Fa0       | 192.168.30.3    | 255.255.255.0     | 192.168.30.0/24 |





## ⚙️ Router Configurations

### Router0
```bash
Router0# show running-config
!
interface FastEthernet0/0
 ip address 192.168.10.1 255.255.255.0
 no shutdown
!
interface Serial0/0
 ip address 10.0.0.1 255.255.255.252
 no shutdown
!
ip route 192.168.20.0 255.255.255.0 10.0.0.2
ip route 192.168.30.0 255.255.255.0 10.0.0.2
ip route 11.0.0.0 255.255.255.252 10.0.0.2
```
*(Repeat for Router1 and Router2)*



## 🔀 Static Routes Explained

Static routing means each router is **manually told** where 
to send packets for networks it doesn't directly know about.

### Routing Logic Diagram:

PC0 (192.168.10.x) 
  → Router0 → [Serial: 10.0.0.0/30] 
  → Router1 → [Serial: 11.0.0.0/30] 
  → Router2 → PC4/PC5 (192.168.30.x)



## ✅ Testing & Verification

### Ping Tests Performed:
| Source | Destination      | Result |
|--------|------------------|--------|
| PC0    | 192.168.20.2     | ✅ Success |
| PC0    | 192.168.30.3     | ✅ Success |
| PC2    | 192.168.10.2     | ✅ Success |
| PC4    | 192.168.10.3     | ✅ Success |

### Verification Commands Used:
```bash
show ip route          # Verify routing table
show ip interface brief # Check interface status
ping 192.168.30.2      # End-to-end connectivity test
tracert 192.168.30.2   # Trace the path
```


## ▶️ How to Run This Project

1. Download and install **Cisco Packet Tracer** (v8.x recommended)
2. Clone this repository:
```bash
git clone https://github.com/yourusername/static-routing-project
```
3. Open `final-static-routing.pkt` in Packet Tracer
4. Switch to **Simulation Mode** to observe packet flow
5. Send pings between PCs to test connectivity




## 💡 Key Learnings

- Understood how static routes are manually configured
- Learned the difference between /30 (WAN) and /24 (LAN) subnets
- Practiced serial interface configuration on Cisco routers
- Verified end-to-end connectivity across 3 different networks
- Understood the role of gateway IPs and next-hop addresses
