# Introduction
**Name:** Hadi Saghir
**Student Credentials:** hs223um

**Short Project Overview:**
This project aims to convert the BOSCH Styline TKA8013 coffee machine into a smart appliance. By leveraging IoT principles and following the course provided roadmap, I will demonstrate proficiency in development environment & device configuration, network connectivity, and data visualization to reach the objectives of my project.

**Time Estimate:**
Approximately 4-8 hours, less if you worked with these programs before

![w/o LoRa](https://hackmd.io/_uploads/HkKBov2_3.jpg)
## Objective:

**What and Why**
The objective of this project is to showcase how existing appliances, like the BOSCH Styline TKA8013 coffee machine, can be transformed into smart devices while retaining their simplicity, affordability, and user-friendly interface. The functionality that will be added are as follows:

1. Brew: Start brewing coffee instantly upon command.
2. Brew: Schedule brewing in advance using time or using a preset timer.
3. Warm: keep the coffee warm for a certain amount of time
4. Warm: keep the coffee warm until manually instructed otherwise.
5. Notify: Receive a notification when the coffee is ready to be served.
6. Maintenance: Generate a temperature report to ensure the coffee machine maintains optimal brewing temperature.
7. Maintenance: Generate a temperature report to ensure the coffee machine maintains highest warm temperature in keep warm mode.

**The Purpose**
The purpose of this project is simple: Buy the Coffee Machine for its Coffee Making Ability and Make it Smart! we want to avoid unnecessary design complexities and proprietary systems that are often associated with energy-consumption and high prices.

**Insight**
This ambitious project has given me invaluable insights into the world of creating a smart and efficient network infrastructure. By incorporating a fully locally-hosted server, I have learned the importance of building a secure and robust network that can accommodate a multitude of devices. This project has opened my eyes to the complexities associated with avoiding unnecessary design complexities and proprietary systems, while still achieving energy efficiency. Through the course syllabus, I have gained a deep understanding of IoT, microcontroller micropython programming, sensor data collection, IoT infrastructure, MQTT messaging protocols, connectivity (LoRaWAN and WiFi), data visualization, time series databases. The hands-on nature of the course has allowed me to develop practical skills in developing an IoT project from conception to implementation. 


# Getting Started

This section will cover the required materials  and computer setup.

## Material

The following materials have been obtained from the following kits:

* [LNU Starter kit](https://www.electrokit.com/produkt/start-kit-applied-iot-at-linnaeus-university-2023/) (399 SEK)
* [LNU Addon kit](https://www.electrokit.com/produkt/addon-kit-applied-iot-at-linnaeus-university-2023/) (349 SEK) [Option LoRa]
* [Sensor Kit – 25 modules](https://www.electrokit.com/produkt/sensor-kit-25-moduler/) (299 SEK)

| Type         | Material                   | Description                                            |
| ------------ | -------------------------- | ------------------------------------------------------ |
| Sensor       | Photo Resistor             | Analog light measure                                   |
| Sensor       | DH11                       | Temperature & Moisture                                 |                                 |
| ---          | ---                        | ---                                                    |
| Actuator     | RGB LED                        | Light-emitting diode to simulate state and the press of a button |
| ---          | ---                        | ---                                                    |
| Connectivity | M5Stack LoRa module 868MHz | Optional                                                |
| ---          | ---                        | ---                                                    |
| Controller   | Raspberry Pi Pico WH       | Microcontroller                                        |
| ---          | ---                        | ---                                                    |
| Circuit      | Jumpwire                   | Male-to-Male and Male-to-Female                        |
| Circuit      | Breadboard                 | 840 pins connections                                   |

1. **Photo Resistor:** The Photo Resistor is an analog sensor used to measure the intensity of light in the surrounding environment. It provides valuable data for monitoring the state of the coffee machine as the Bosch emits light when on.

2. **DHT11**: The DHT11 sensor is a versatile component capable of measuring both temperature and humidity levels. It will be used to measure the temperature of the coffee for temperature controll and statistics.

3. **RGB LED** : the red LED indicates the "off" state, the green LED represents the "on" state, and the blue LED simulates a button press. This approach provides flexibility for users to choose a button press component that suits their machine and avoids the need for additional components beyond those acquired at the beginning of the course, simplifying the implementation. By leveraging the LED's properties, we visually communicate states: the red LED is off for "off," the green LED is on for "on," and the blue LED represents a simulated button press.

4. **M5Stack LoRa module 868MHz:** This LoRa module operates at a frequency of 868MHz and is designed for long-range, low-bandwidth data transmission. Optional for energy preservation.

5. **Raspberry Pi Pico WH:** The Raspberry Pi Pico WH is a microcontroller board with built-in headers, making it easy to connect and program. It offers a compact yet powerful platform for controlling and interacting with the various components.

6. **Jumpwire:** Jumpwires are essential circuit-building components used to establish connections between different parts of an electronic circuit. Male-to-male and male-to-female jumpwires facilitate the flow of signals and power between sensors, actuators, and controllers.

7. **Breadboard:** A breadboard is a prototyping platform featuring interconnected clips or sockets that allow for the temporary connection of electronic components. It provides a convenient way to assemble and test circuits without soldering, making it ideal for rapid experimentation and design iteration.

## Computer setup

The project incorporates several services to achieve interoperability of a locally-hosted IoT solution. The software stack includes Thonny as the programming environment for the Pico board, Helium for establishing connectivity, Mosquitto as the MQTT broker, Node-RED as the cloud platform, InfluxDB for database, Grafana for visualization, and Telegram bots  as an interface to the network for remote control of the coffee machine and visualization of data. These services work together to enable seamless integration and functionality across the IoT ecosystem.

After multiple attempts that included, but not limited to, semi-locally hosting, hosting services onatively on my Windows computer, using Adafruit, using http, using VMs and dockers containers, the finals version is a fully locally hosted. I have configured using docker-compose with additional setup required.

1. **Download Thonny:** follow the [tutorial](https://hackmd.io/@lnu-iot/SyTPrHwh_) provided by LNU

2. **Update Firmware on Pico:** follow the [tutorial](https://hackmd.io/@lnu-iot/rkFw7gao_) provided by LNU

3. **Docker:** 

     Hopefully, I can add more scripts to full fully automate deployment. Follow this [tutorial](https://github.com/Hadi-Saghir/1DT305_IoT_Project/blob/main/Docker/Docker%20setup.txt) i created for setting up. I've included setup tutorials on how to reconfigure things found below.

    **Login credentials** to Grafana, InfluxDB or Mosquitto/Management center:
    * username: hadi
    * password: Iminyourarea

    **MQTT Client credential:**
    * username: hadsag
    * password: Testuser1

    I have configured setup. However, addition configuration is needed. "1DT305_IoT_Project/Docker" has a folder for every service with tutorials/reconfiguration if you dont want me in your area. Set them up in the following order:
        1. **Mosquitto** ([to complete the setup](https://github.com/Hadi-Saghir/1DT305_IoT_Project/blob/main/Docker/mosquitto/setup.txt), [ to reconfigure](https://github.com/Hadi-Saghir/1DT305_IoT_Project/blob/main/Docker/mosquitto/setup.txt))
        2. **influxdb** ([to complete the setup](https://github.com/Hadi-Saghir/1DT305_IoT_Project/blob/main/Docker/influxdb/setup.txt), [to reconfigure](https://github.com/Hadi-Saghir/1DT305_IoT_Project/blob/main/Docker/influxdb/reconfigure.txt))
        3. **Grafana** ([to complete the setup](https://github.com/Hadi-Saghir/1DT305_IoT_Project/blob/main/Docker/Grafana/setup.txt), [to reconfigure](https://github.com/Hadi-Saghir/1DT305_IoT_Project/blob/main/Docker/Grafana/reconfigure.txt))
        4. **NodeRED** ([to complete the setup and import flow](https://github.com/Hadi-Saghir/1DT305_IoT_Project/blob/main/Docker/NodeRED/setup.txt))


9. **Helium (Option LoRa):**

    1. Setup Helium (MQTT integration, Function and Flow) can be found on [Git](https://github.com/Hadi-Saghir/1DT305_IoT_Project/blob/main/Helium/setup.txt.txt). The usage of my json format and decoder is optional, but I found their default Json to be verbose and two-dimensional, which is so unnecesaary.

All code and files can be found in [Github](https://github.com/Hadi-Saghir/1DT305_IoT_Project)

# Assembly

This part will include how to assemble the circuit with the materials mentions above. This includes: "Putting Everything Together", "Code", Transmitting the Data"

## Putting Everything Together

This section will include who to put the pico together, i.e. hardware. I'm using free software so i had to get a little creative with drawing. 

OBS! The black is ground and red is the 3V3, some breadboards have different layouts, which can be confusing.

**Circuit Diagram**
![Diagram](https://hackmd.io/_uploads/r1r0-CkKn.png)




**Electrical calculation**

To obtain accurate power consumption values, we need to use power meter. To provide an electrical calculation for this IoT project, I will need to estimate the power consumption of each component with some assumptions based on the [information provided by electrokit ](https://www.electrokit.com/uploads/productfile/41015/User_guide.pdf)and browsing the web, we can calculate the following:

The power consumption can be calculated by using Ohm’s law: P = V^2 / R

1. The **photo resistor** module has a resistance of 10 kΩ and operates at 3.3V. P ≈ 0.001 W 
2. The **DHT11** module operates at 3.3V and has a maximum current of 2.5mA. P ≈ 0.3W (active) and 0.06W (idle). 
3. The **RGB LED** module operates at an operating voltage of 5V and three 150Ω limiting resistors. P ≈ 0.5W
4. The **M5Stack LoRa module 868MHz**  operates at 3.3V or 5V and has a maximum current of 250mA. P ≈ 0.1W to 0.8W, depending on the operating mode, frequency, and transmit power.
5. The **Raspberry Pi Pico WH** operates at 3.3V or 5V. The maximum current is not specified, but it is recommended to use a power supply that can provide at least 500mA. P ≈ 2.5W or 1W, depends on activity.

The total power consumption of the circuit can be estimated by adding up the power consumption of each component, assuming they are all operating at the same time:

***P total*** = P photoresistor + P DHT11 + PLED + P LoRamodule + P PicoWH

Using the **maximum values** for each component, we get:

***P total*** = 0.001 + 0.3 + 0.5 + 0.8 + 2.5 = **4.101W**

Using the **minimum values** for each component, we get:

***P total*** = 0.001+0.06+0.1+0.1+1 = **1.271W**

To achieve lower power consumption, we need to program the Pico to enter deep sleep and idle mode when it is not actively performing tasks or interacting with external components. 

I watched tests online of the energy efficiency of the pico when in idle and sadly it is not efficient, so i will opt for deepsleep. I decided to make it not a very responsive coffee machine in order to get more energy efficiency. The result I could find are:

**P active:** 60mA (WiFi and Pinging MQTT)
**P idle:** 39 mA
**P deepsleep:** 16 mA

I will make the coffee machine deepsleep after the following events.

* Deepsleep from 22 to 8
* Deepsleep 2 hours after brewing and warming
* Deepsleep 20 mins then check for request

## Platform

For this project, I carefully considered various platforms and services to create an efficient and seamless IoT solution. After exploring different options, I made specific choices based on functionality, ease of use, energy efficiency, and personal preferences.

![Platform](https://hackmd.io/_uploads/SkOXltYuh.png)


**Helium (Option LoRa):**
Both Helium and The Things Network offer power-efficient communication and enable long-range connectivity with minimal power consumption. By utilizing LoRaWAN through Helium, the IoT solution can operate on low power, enabling devices to conserve energy effectively. 

I have setup both but opted for Helium despite the cost disadvantage (1$ for now). Helium offered two two main advantages in my use- case:
1. pay-per-use  ensures more reliable and available connectivity, even in lower coverage areas. I was able to join after walking around my apartment a bit.
2. The decentralized infrastructure allow for more security, control and scalability, in turn for the cost of setup. For my specific use-case, I was able to integrate my MQTT Endpoint instead of having to use The Network Things own MQTT Service. The other options were very inconvenient, such as webhooks or official cloud providers AWS/Azure. TTN free was very unflexible!

![Helium flow](https://hackmd.io/_uploads/B1NqDDndh.png)



I would recommend using your own gateway for privacy, efficiency, and performance. I only have a WiFi gateway, so I tested with providers such as Helium and TTN. 

OBS! Helium doesn't natively support SSL, so you have to expose port 1883 (default docker-compose has 1883 open).

You can pay to download and host a helium console locally following this [tutorial](https://docs.helium.com/use-the-network/run-a-network-server/run-console/), but it won't be covered in this report as I don't want to pay.

**MQTT Broker:**

In terms of messaging protocol, I opted for MQTT (Message Queuing Telemetry Transport) due to its lightweight nature and energy efficiency. 

I encountered challenges when attempting to use Mosquitto Eclipse on my Windows system. Despite successfully testing the pub-sub test on my local machine, I experienced difficulties when other machines tried to connect. I tried to containerize it using Docker and even setup a Ubuntu VM. I also integrated MQTTExplorer. After investing absurdly significant time and effort into debugging, I switched to HiveMQ for reliable, hassle-free connectivity. HiveMQ provided a more stable, secure (utilizing SSL), and hassle-free experience, ensuring seamless communication between devices. This help decouple Operating System (OS) interference and enables less dependancies for easier replication of the project.

![HiveMQ](https://hackmd.io/_uploads/By5VcvXd3.png)

After finishing the project first draft, I read and watch multiple hours worth of material on docker and network because i didn't want to have a semi-locally hosted. I finally understood how it works and how i can use docker-compose to create a network bridge between the different containers and how to expose the ports. I containerized all my services and created a decoupled environment for high interoperability and control the network to ensure security and privacy. In addition, I learned learned how to create SSL certificates to ensure maximuim security, so I didn't compromise on security.

I integrated Cedalo Management Center for more convenient management of Mosquitto. However, I wrote a [tutorial](C:\Users\hadis\Desktop\Git\IoT\1DT305_IoT_Project\Docker\mosquitto\config) and [cmds](https://github.com/Hadi-Saghir/1DT305_IoT_Project/blob/main/Docker/mosquitto/commands.txt) for ubuntu if so wish to do something else. I added to the tutorial how to setup SSL in mqtt_connector_import.json file in mangentcenter to enable SSL, making the only service that requires port 1883 to be open is Helium.

**Node-RED:**
When it came to selecting a cloud platform, I opted for Node-RED. This choice was influenced by my familiarity with Node.js and my attraction to the block language for flow management. Node-RED allowed me to easily design and implement the necessary workflows and integrations within the IoT ecosystem.

In addition, Node-RED enables me to focus on flow creation by abstracting communication concepts by using nodes, such as MQTT, Telegram and influxdb. I did have to configure everything else myself, such as tables and measurements in influxdb, setting up the Telegram bot, and the topic tree for MQTT.

The first identified design pattern in Node-RED is the start, started and done state machine to create a responsiveness for the servers interface (Telgram).

On GitHub, you can find a file you can use to import the project onto your own Node-RED instance (You need to setup connection to your own MQTT, influxdb and Telegram connections).

**Getting Started:**
![start](https://hackmd.io/_uploads/Skya8Pmu3.png)
**Brewing:**
![brew](https://hackmd.io/_uploads/SyeEUDmun.png)
**Keep warm:**
![warm](https://hackmd.io/_uploads/ByCUID7_n.png)

**Server option:**
I would highly recommend using a Rasperbery Pi to host the platforms because of lower energy consumption. My monster of a desktop/Laptop consumes too much unneccessary energy, using Corsair RM850e 850W(Desktop) and 300W Lenovo(Laptop). 

This server is designed with scalability in mind, allowing for easy configuration and integration into larger network systems, rather than being limited to a single device.

## Code

The complete source code can be found in [my GitHub repository](https://github.com/Hadi-Saghir/1DT305_IoT_Project). The code is structured into one main files:

Logic:
- [main.py](https://github.com/Hadi-Saghir/1DT305_IoT_Project/blob/main/Pico/main.py)

Handlers(utils/):
- [MQTTHandler.py](https://github.com/Hadi-Saghir/1DT305_IoT_Project/blob/main/Pico/utils/MQTTHandler.py)
- [WiFiConnectionHandler.py](https://github.com/Hadi-Saghir/1DT305_IoT_Project/blob/main/Pico/utils/WiFiConnectionHandler.py)
- [LoRaConnectionHandler.py](https://github.com/Hadi-Saghir/1DT305_IoT_Project/blob/main/Pico/utils/LoRaConnectionHandler.py)
- [SensorHandler.py](https://github.com/Hadi-Saghir/1DT305_IoT_Project/blob/main/Pico/utils/SensorHandler.py)
- [ActuatorHandler.py](https://github.com/Hadi-Saghir/1DT305_IoT_Project/blob/main/Pico/utils/ActuatorHandler.py)

Keys:
- secrets.py (no link)

In addition, there are some import libraries, which reside in a (lib/) directory and are:

- [Micropython-umqtt.simple.py](https://pypi.org/project/micropython-umqtt.simple/)

I identified design patterns that could promote reusability and scailability.

**Class diagram**
![class diagram](https://hackmd.io/_uploads/BJMA0r3_2.png)

```
Start
|
|--> Initialize Machine
|    |
|    |--> Initialize WiFiHandler
|    |    |
|    |    |--> Initialize connection
|    |    
|    |--> Initialize MQTTHandler
|    |    |
|    |    |--> Initialize MQTTClient
|    |
|    |--> Initialize SensorHandler
|    |    |
|    |    |--> Initialize Pins and ADC
|    |
|    |--> Initialize ActuatorHandler
|
|--> Set MQTT message handler
|
|--> Loop
|    |
|    |--> Check MQTT connection
|    |    |
|    |    |--> Reconnect if not connected
|    |    |
|    |    |--> Setup MQTT subscriptions
|    |    |
|    |--> Check for incoming MQTT messages
|    |    |
|    |    |--> Publish signal of acknowledgment
|    |    |
|    |    |--> Handle message
|    |    |    |
|    |    |    |--> Run brewing or warming process
|    |    |    |
|    |    |    |--> Publish data
|    |    |
|    |    |--> Publish signal of completion
|    |
|    |--> Check for received commands
|    |    |
|    |    |--> Increase command counter
|    |    |
|    |    |--> Check command counter limit reached
|    |    |    |
|    |    |    |--> Enter deep sleep 2 hour
|    |    |    
|    |--> Check if it's night time
|    |    |
|    |    |--> Enter deep sleep() 10 hour
|    |    |
|    |--> Else 
|    |    | --> Enter deep sleep() 20 mins
|    |
|
End

```

## Trasmitting Data

The data  is transmitted on a local network using a Wi-Fi  as the main connection. Wi-Fi was chosen as the wireless protocol due to its availability and compatibility with the existing infrastructure. I was able to setup LoRa by walking around and while LoRa would have been an energy-efficient option, its limited coverage in the project area made Wi-Fi the more practical choice. Despite this, this project has scaibility and flexibility in mind so both are configured.

To facilitate the data transmission, the project utilizes the MQTT (Message Queuing Telemetry Transport) protocol. MQTT is a lightweight and efficient messaging protocol designed for IoT applications. It allows for reliable and asynchronous communication between the IoT devices and the server, ensuring the delivery of messages even in unreliable network conditions. MQTT's publish-subscribe model enables efficient data distribution, where the devices publish their data to specific topics, and the server or other subscribed clients receive the data from those topics. The data is trasmitted in the following frequency:

**Signaling data communication (initiated by user):** (qos = 2)
1. Signal is sent when *brewing starts* and when the *brewing is done*.
2. Signal is sent when *warming starts* and when the *warming is done*.

**Readings is sent at specific events:** (qos = 0)
1. *After brewing is done*, a temperature reading is sent to ensure coffee is brewing at the desired temperature.
2. *During the coffee-warming phase*, temperature and humidity measurements of the coffee are sent every minute to monitor if its stays in the desired temperature.


I have successfully configured SSL in my third draft to enable the utilization of TLS, effectively bolstering the security of our communication channels.

The choice of Wi-Fi and MQTT has implications for device range and battery consumption. Wi-Fi offers a relatively shorter range compared to other wireless protocols like LoRa. However, since the project is deployed in an area with Wi-Fi coverage, this limitation is mitigated. In terms of battery consumption, Wi-Fi tends to consume more energy compared to low-power protocols like LoRa. However, given the specific requirements of the project and the availability of Wi-Fi infrastructure, the trade-off between energy efficiency and connectivity convenience was made in favor of Wi-Fi.

**The code is available for LoRa and WiFi** Make sure to import `utils/LoRaConnectionHandler.py` and adjust some comment/uncomment necessary lines:
```
        temperature, humidity = self.sensor_handler.read(Sensor.DH11)
        #self.lora.pub_sensor_values("b", temperature, humidity)
        self.mqtt_handler.publish_message(b'brew/done', "Brew process completed")
        self.mqtt_handler.publish_message(b'brew/done/sensor/temp', str(temperature))
```

**Beware!** LoRa is unit and integration tested, but not system tested. Testing was done in an earlier version (I honestly lost track from the amount of times i revised and refactored). I configured it in the park away from the project site (Home).

## Presenting the Data

**influxdb:**
To store and manage the collected data, influxDB will be utilized as the database solution. influxDB excels in handling time-series data, making it a perfect fit for this IoT project. It provides efficient storage and retrieval of time-stamped data points. This will allow me with ease to retreive data on temperature through time to see if the coffee is being brewed at optimal temperature. In addition, it is compatiable with Node-RED. The following trigger is used in the following scenarios mention above:
1. *After brewing is done*, a temperature reading is sent to ensure coffee is brewing at the desired temperature.
2. *During the coffee-warming phase*, temperature and humidity measurements of the coffee are sent every minute to monitor if its stays in the desired temperature.

![trigger](https://hackmd.io/_uploads/r10Ag8cd3.png)

The length of retention is set to 1 year in docker-compose.yml file:
    `DOCKER_INFLUXDB_INIT_RETENTION=365d`

influxdb uses its own query language, which is different from the most popular query languages, and takes some time to learn.

```
from(bucket: "brew")
  |> range(start: 0)
  |> filter(fn: (r) => r._measurement == "temp")
```

![influxdb](https://hackmd.io/_uploads/rk9bj8hdn.png)


**Grafana**
Grafana is chosen as the visualization and monitoring tool for the IoT project due to its compatibility with InfluxDB, the selected database solution. Its native integration with InfluxDB ensures seamless data retrieval and visualization, enabling a smooth workflow when working with time-series data. I didn't scrutinize other option as I primarly want to visualize things on Telegram for convenience.

![Grafana](https://hackmd.io/_uploads/r1YIbgZFn.png)



**Telegram:**
Lastly, I utilized Telegram bots for remote control of the coffee machine and data visualization. I preferred Telegram over other messaging platforms, such as Discord, due to its simplicity and user-friendly UI. Having Telegram installed on my phone allowed me to conveniently monitor and interact with the IoT system from anywhere.

Flow

![trigger](https://hackmd.io/_uploads/By1CbUqdn.png)
Chat

![Telegram](https://hackmd.io/_uploads/SJnPSstd2.png)

# Finalizing the Design & Reflections


The IoT Coffee Brewing System project has been successfully implemented, resulting in a smart and automated coffee brewing solution from the convenience of a Telegram. The system combines various sensors, connectivity options, and two user-friendly interface to enhance the coffee making experience.

**Key Features:**
1. Wireless Monitoring: The system allows individuals to monitor the temperature and the humidity of the coffee brewing temperature and warming. Users can conveniently check the status of their coffee from anywhere.

1. Remote control: The system allows individuals to control their coffee machine using Telegram. You can brew coffee and turn of the machine once done to save energy. You can keep the coffee warm for as long as you want.

2. More control: The system allows user more options such as scheduling and timers to when you want to have your coffee and specified durations to keep your coffee warm

4. Energy efficiency: Once the brewing process is complete, an alert is sent to the user's mobile device and the machine is turned automatically off for energy saving.

4. Intuitive visualization of data: A user-friendly dashboard for in-depth monitoring, but allows for the  convenience of seeing the information anywhere you want using Telegram

## Photos

![Photo resistor uncovered](https://hackmd.io/_uploads/ByFBiDh_n.jpg)
![w LoRa](https://hackmd.io/_uploads/HJYHiw2_n.jpg)
![w Lora](https://hackmd.io/_uploads/r1FSivnOh.jpg)
![bird view](https://hackmd.io/_uploads/SyYSovn_h.jpg)

## Video Presentation

[Link to Youtube video](https://www.youtube.com/watch?v=c63xlWkW_jY)

## Overall Assessment
This project helped me learn a couple of valuable skills, and I'm really happy with the results. Here are some of the key things I learned:

* I learned how to use **Docker** and gained proficiency in writing Docker Compose files.
* I deepened my **understanding of networks**, including the concepts of frequencies, bandwidth, ports and security. I also learned how to create bridges in Docker.
* I learned how to effectively use **Pub/Sub**.
* **locally-hosting** on Docker was a fascinating and rewarding experience.
* I gained **practical knowledge** in working with sensors and actuators.
* I realized the importance of **energy efficiency** in making IoT a prominent feature of the future.

## Areas for Improvement I wished to implement
1. **More appropriate sensors:** The DH11 does not measure the temperature of the coffee accurately. The photo resistor needed to be configured using software and the hardware needed to be in an isolated environment. Proving an ugly, constrictive appendage on the dimly lit start button that isn't fool proof (100% accurate). It was the only sensor available to able to work around not ruining the coffee machine and getting evicted.

2. **Enhanced energy efficiency:** While the current implementation utilizes Wi-Fi connectivity, exploring power-efficient alternatives like LoRaWAN relay module with extended range could further optimize energy consumption, particularly in scenarios where Wi-Fi coverage is limited.

3. **Integration with voice assistants:** Integrating the system with popular voice assistants like Amazon Alexa or Google Assistant would provide additional convenience and hands-free control options for users. I don't own one but i see how voice assistants can be used now with this smart coffee machine. However, it is too costly for me.

4. **Using script:** Scripts are very powerful tools for automating deployment and configuration. For example, using cmd such as `influx bucket create -n brew -r 365d -o hadsag`, i can automate setup of influxdb. This elimiates risk of miscommunication.
