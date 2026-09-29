from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
app=FastAPI(title='WattWise AI API',version='1.0.0')
app.add_middleware(CORSMiddleware,allow_origins=['*'],allow_methods=['*'],allow_headers=['*'])
MACHINES=[{'name':'CNC Line 01','energy':86,'baseline':78,'idle':7,'temperature':42,'output':184},{'name':'Press Line 02','energy':112,'baseline':96,'idle':19,'temperature':47,'output':176},{'name':'Compressor 02','energy':74,'baseline':51,'idle':62,'temperature':39,'output':0},{'name':'Assembly 04','energy':63,'baseline':60,'idle':11,'temperature':41,'output':151},{'name':'Packaging 01','energy':51,'baseline':50,'idle':5,'temperature':38,'output':210}]
@app.get('/api/health')
def health(): return {'status':'ok','service':'WattWise AI'}
@app.get('/api/overview')
def overview():
 total=sum(x['energy'] for x in MACHINES);base=sum(x['baseline'] for x in MACHINES)
 anomalies=[]
 for x in MACHINES:
  change=(x['energy']-x['baseline'])/x['baseline']*100
  if change>=15 or x['idle']>=30: anomalies.append({**x,'change_pct':round(change,1)})
 return {'energy_kwh':total,'baseline_kwh':base,'variance_pct':round((total-base)/base*100,1),'estimated_cost_inr':round(total*8.2),'co2_kg':round(total*.72,1),'anomalies':anomalies,'machines':MACHINES}
@app.get('/api/copilot')
def copilot(question:str):
 q=question.lower()
 if 'compressor' in q:return {'answer':'Compressor 02 is the priority anomaly. It is drawing 74 kWh against a 51 kWh baseline, with 62% idle time and zero output. Review scheduling, leaks and unloaded running.'}
 if 'save' in q:return {'answer':'A conservative simulated estimate is ₹8,400/month if high-idle equipment moves closer to baseline. Replace this with actual tariff and telemetry before operational use.'}
 return {'answer':'The largest deviation is Compressor 02. Its energy is about 45% above baseline while output is zero. Excessive idle operation is the strongest signal in this demo dataset.'}
