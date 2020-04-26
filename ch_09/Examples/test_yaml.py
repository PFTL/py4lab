import yaml

with open('experiment.yml', 'r') as f:
    e = yaml.load(f, Loader=yaml.FullLoader)

print(e['Experiment'])
for k in e['Experiment']:
    print(k)
    print(e['Experiment'][k])
    print(10*'-')