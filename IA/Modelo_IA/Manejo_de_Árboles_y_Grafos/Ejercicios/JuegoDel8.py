from Grafos.JuegoDel8Grafo import PuzleN

g = PuzleN(8)
final = "1-2-3-4-5-6-7-8-0"
inicial = "2-7-0-4-5-3-8-6-1"
#g = PuzleN(15)
#final = "1-2-3-4-5-6-7-8-9-10-11-12-13-14-15-0"
#inicial = "14-1-5-4-2-7-6-8-9-10-15-12-13-3-11-0"   # (762 
g = PuzleN(15)
final = "1-2-3-4-5-6-7-8-9-10-11-12-13-14-15-0"
inicial = "11-3-0-1-10-12-5-13-7-9-4-8-6-15-2-14" # 1121 pasos 
#g = PuzleN(24)
#final = "1-2-3-4-5-6-7-8-9-10-11-12-13-14-15-16-17-18-19-20-21-22-23-24-0"
#inicial = "11-3-0-1-10-12-5-21-13-20-7-9-4-19-8-6-15-18-2-14-17-16-24-22-23" # 1121 pasos 

ret = g.recorre_grafo(nodo_inicial=inicial, nodo_destino=final, modo="avaricioso")
if ret: 
    ruta = g.genera_ruta(final)
    print(f"Encontrada solución en {len(ruta)} pasos:\n{ruta[::-1]}")
else: print("Se exploró sin encontrar solución")