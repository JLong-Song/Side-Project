//---------------------------------------------------------------------------
#include "Remote_Block.h"
#include "stdio.h"
#include <tlhelp32.h>
#include <dir.h>
#include <dos.h>
#include <sys/timeb.h>
//---------------------------------------------------------------------------
#pragma package(smart_init)
#pragma resource "*.dfm"

TRemoteBlock *RemoteBlock;
TStringList* exe_name;
//---------------------------------------------------------------------------
__fastcall TRemoteBlock::TRemoteBlock(TComponent* Owner)
	: TService(Owner)
{
}

TServiceController __fastcall TRemoteBlock::GetServiceController(void)
{
	return (TServiceController) ServiceController;
}

void __stdcall ServiceController(unsigned CtrlCode)
{
	RemoteBlock->Controller(CtrlCode);
}
//---------------------------------------------------------------------------
void __fastcall TRemoteBlock::ServiceCreate(TObject *Sender)
{
    Sleep(1000);
    char rbuf[256];
    String S;
    GetSystemDirectory(rbuf,255);//取得Windows的系統資料夾名稱
    S = rbuf; S += "\\cond.ini";
    if(!FileExists(S)){
        FILE *app;
        app = fopen(S.c_str(),"w");
        fprintf(app, "TeamViewer\nAnyDesk\n");
        fclose(app);
    }
    exe_name = new TStringList();
    exe_name->LoadFromFile(S);//阻擋名單
}
//---------------------------------------------------------------------------
void __fastcall TRemoteBlock::ServiceExecute(TService *Sender)
{
    char rbuf[256];
    String S;
    GetSystemDirectory(rbuf,255);//取得Windows的系統資料夾名稱
    S = rbuf; S += "\\cond.ini";
    while(!Terminated){
        ServiceThread->ProcessRequests(false);
        for(int i = 0; i < exe_name->Count; i++){
            Block_Application(exe_name->Strings[i] + ".exe");
        }
        exe_name->Clear();
        exe_name->LoadFromFile(S);
        Sleep(1000);
    }
}
//---------------------------------------------------------------------------
void __fastcall TRemoteBlock::Block_Application(String processName)//阻擋遠端
{
	PROCESSENTRY32 entry;
    entry.dwSize = sizeof(PROCESSENTRY32);
    HANDLE snapshot = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, NULL);
    if(Process32First(snapshot, &entry)){
        while(Process32Next(snapshot, &entry)){
            String binPath = entry.szExeFile;
            if(binPath.Pos(processName) != 0){ //找到遠端程式
                HANDLE Process;
                Process = OpenProcess(PROCESS_ALL_ACCESS, FALSE, entry.th32ProcessID);
                TerminateProcess(Process, 0);  //強制中斷
                CloseHandle(Process);
                WriteLog("已阻擋 " + binPath);
            }
        }
    }
    CloseHandle(snapshot);
}
//---------------------------------------------------------------------------
void __fastcall TRemoteBlock::WriteLog(String txt)//寫記錄
{
    String S, Fn;
    struct date now_d;
    struct time now_t;
    FILE *fp;
    struct timeb Now_Time;
    unsigned long cal_msec;

    ftime(&Now_Time);
    cal_msec = (long)(1000.0 * (Now_Time.time) + (Now_Time.millitm));

    getdate(&now_d);
    gettime(&now_t);

    ForceDirectories("D:\\RemoteBlock");
    ForceDirectories("D:\\RemoteBlock\\log"); //強制建立資料夾，若已存在則忽略

    Fn.sprintf("D:\\RemoteBlock\\log\\%04d%02d%02d.log",now_d.da_year,now_d.da_mon,now_d.da_day);
    fp = fopen(Fn.c_str(), "a");
    S.sprintf("%02d:%02d:%02d(%u) %s\n", now_t.ti_hour, now_t.ti_min, now_t.ti_sec, cal_msec, txt);
    fprintf(fp, S.c_str());
    fclose(fp);
}
//---------------------------------------------------------------------------
void __fastcall TRemoteBlock::ServiceStop(TService *Sender, bool &Stopped)
{
    WriteLog("服務關閉");
}
//---------------------------------------------------------------------------
void __fastcall TRemoteBlock::ServiceStart(TService *Sender, bool &Started)
{
    WriteLog("服務開啟");
}
//---------------------------------------------------------------------------
