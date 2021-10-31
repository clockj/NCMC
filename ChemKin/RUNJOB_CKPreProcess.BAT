REM Generated Batch Job Command File

REM get the runtime environment defined

CALL "D:\Ansys\ANSYS Inc\v190\reaction\chemkinpro.win64\bin\run_chemkinpro_env_setup.bat"
REM cd to the Working Directory for this job
D: && cd \OneDrive-sjtu\OneDrive - sjtu.edu.cn\Projects\Zhou_Dezhi\Project\Preprocessing\Project_KM2\ChemKin
SET JAVA_RPS=9675@localhost
SET JAVA_RSI=LAPTOP-I3289PAN-zclock-10936-012878

REM RUN THE JOB AND CAPTURE EXIT STATUS

CKPreProcess.EXE -i "D:\OneDrive-sjtu\OneDrive - sjtu.edu.cn\Projects\Zhou_Dezhi\Project\Preprocessing\Project_KM2\ChemKin\CKPreProc_C2H4.input"
exit %errorlevel%
