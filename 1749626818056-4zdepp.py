import asyncio,time,random,json
import subprocess,os,zipfile,shlex



def unzip_file(zip_path, extract_path):
    try:
      with zipfile.ZipFile(zip_path, 'r') as zip_ref:
          zip_ref.extractall(extract_path)
      print(f"Successfully extracted '{zip_path}' to '{extract_path}'.")
    except FileNotFoundError:
        print(f"Error: File not found at '{zip_path}'.")
    except zipfile.BadZipFile:
        print(f"Error: Invalid zip file format for '{zip_path}'.")


tid = input("code create bot [}>").split()
if tid[0] == "new":
	porchn_md = tid[1]
	
	if os.path.exists(porchn_md) == False:
		zip_file = "U.zip"
		
		da = int(time.localtime().tm_mday) + int(tid[3])
		print(da)
		tedad_join = tid[5]
		dae = {"day":da,"join":int(tedad_join),"off_on":"on"}
		
		unzip_file(zip_file, tid[1])
		open(f"{porchn_md}/settting_asl.json","w").write(json.dumps(dae))
		print("ok")

		subprocess.run(["python3",f"{porchn_md}/bot.py",porchn_md])
	else:
		print("فایل موجود میباشد")
elif tid[0] == "edit":
	id = tid[1]
	if os.path.exists(id) == True:
		
		da:dict = json.loads(open(f"{id}/settting_asl.json").read())
		da.update({"day":tid[3],"join":tid[5]})
		open(f"{id}/settting_asl.json","w").write(json.dumps(da))
		print("ok")
	else:
		print("login kon")
elif tid[0] == "off":
	id = tid[1]
	if os.path.exists(id) == True:
		da:dict = json.loads(open(f"{id}/settting_asl.json").read())
		da.update({"off_on":"off"})
		print(da)
		open(f"{id}/settting_asl.json","w").write(json.dumps(da))
		print("ok")
	else:
		print("login kon")
elif tid[0] == "update":
	id = tid[1]
	if os.path.exists(id) == True:
	    print("start....")
	    subprocess.run(["python3",f"{id}/bot.py",id])
	
elif tid[0] == "on":
	id = tid[1]
	if os.path.exists(id) == True:
		da:dict = json.loads(open(f"{id}/settting_asl.json").read())
		da.update({"off_on":"on"})
		print(da)
		open(f"{id}/settting_asl.json","w").write(json.dumps(da))
		print("ok")
	else:
		print("login kon")
elif tid[0] == "del":
	id = tid[1]
	if os.path.exists(id) == True:
		os.remove(id)
		print("ok")
elif tid[0] == "info":
	id = tid[1]
	if os.path.exists(id) == True:
		bt = json.loads(open(f"{id}/guid.json","r").read())
		admin = json.loads(open(f"{id}/admin.json","r").read())
		thd = json.loads(open(f"{id}/settting_asl.json").read())
		dab = int(thd) - int(time.localtime().tm_mday)
		 
		text = f"""
تعداد گروه ها : {len(bt)}/{thd['join']}
تعداد روز های باقیمانده : {dab}
تعداد ادمین های ثبت شده : {len(admin)}
		"""
		print(text)