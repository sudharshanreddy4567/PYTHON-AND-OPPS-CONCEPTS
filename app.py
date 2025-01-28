import agent

print(dir(agent))
p1=agent.agent("reddy",30)
print(p1.info())
bos=agent.agent("hio",43)
bos.shooted()
bos.punched()
print(bos.info())