# Application

The main function of this app is to generate a random character based on the game "Elderscrolls Online", it does this buy using the random.choice function in python to generate a skill, alliance and then depending on what alliance you get it will give you a race that belongs to that alliance. 


## Testing

during the testing I ran into an issue where all the tests run and pass when you're in that directory but once you try run pytest from the root only 2/5 pass. I didn't want to spend too much time cfiguring out how to correct this error and risk falling behind so I moved on. 

The tests for service1 tests firstly, if the home page returns a 200 code and secondly, if the overall generate function combining all 4 services work. [Test1](https://i.imgur.com/uoPYfc3.png), [Test2](https://i.imgur.com/F6nkBN6.png)

The tests for service 2 and 3 are basically the same just with different code so make sure it grabs the correct object from that service and sees if it is there. [Test3](https://i.imgur.com/GJEi34m.png), [Test4](https://i.imgur.com/F7nJk50.png)

Finally, the service 4 test checks if you will be given the correct race depending on which alliance you are given. [Test5](https://i.imgur.com/md38LyO.png)

## Test Coverage
[Service_1](https://i.imgur.com/kHy3GvM.png), [Service_2_skill](https://i.imgur.com/GoVGo9H.png), [Service_3_alliance](https://i.imgur.com/HM5XcXp.png), [service_4_race](https://i.imgur.com/LH4Bu1x.png)

## App Architecture 

[App](https://i.imgur.com/UohiAhW.png)

## Trello 
[Trello](https://i.imgur.com/fGSF8xX.png)

## Risk Assessment

During this project we had a pretty huge setback as all the VM's on gcp suddenly stopped working and refused to connect. Thankfully we predicted this could be a risk in the assessment so all damage to the project was minimized as we already had a plan in place. 

[Risk Assessment](https://i.imgur.com/VbElIXA.png)

# Website and rolling update

Attached are images of what the current state of the website. The rolling update will then add css to the html files making the website look more like a professional site. this will include a top nav function, and a colour change.

[Home](https://i.imgur.com/MgS0WVx.png)

[Generate](https://i.imgur.com/ehHIX1n.png)

# Pipeline

The pipeline for this project consists of a main Manager node with a worker node. A VM with Ansible and Jenkins on that connects to the manager and worker, along with the nginx vm. all this is detailed below in the diagram.

[CI-Pipeline](https://i.imgur.com/FYITbiW.png)
