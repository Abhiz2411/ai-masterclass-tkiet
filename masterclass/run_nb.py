import sys,json,time,nbformat,os
from nbclient import NotebookClient
from nbclient.exceptions import CellExecutionError, CellTimeoutError
path=sys.argv[1]; per=int(sys.argv[2]) if len(sys.argv)>2 else 120
nb=nbformat.read(path,as_version=4)
nb.metadata.setdefault("kernelspec",{"name":"python3","display_name":"Python 3","language":"python"})
c=NotebookClient(nb,timeout=per,kernel_name="python3",allow_errors=False,resources={"metadata":{"path":os.path.dirname(os.path.abspath(path))}})
res=[]
with c.setup_kernel():
    for i,cell in enumerate(nb.cells):
        if cell.cell_type!="code": continue
        if not cell.source.strip(): continue
        t=time.time()
        try:
            c.execute_cell(cell,i); res.append((i,"OK",""))
        except CellTimeoutError: res.append((i,"TIMEOUT",f">{per}s"))
        except CellExecutionError as e:
            msg=str(e).strip().splitlines()[-1][:200]; res.append((i,"ERR",msg))
        except Exception as e: res.append((i,"ERR",repr(e)[:200]))
        print(f"c{i} {res[-1][1]} {res[-1][2]} ({time.time()-t:.0f}s)",flush=True)
json.dump(res,open(path+".log.json","w"))
nbformat.write(nb,path.replace(".ipynb",".executed.ipynb"))
