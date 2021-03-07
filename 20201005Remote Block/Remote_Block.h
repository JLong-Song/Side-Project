//---------------------------------------------------------------------------
#ifndef Remote_BlockH
#define Remote_BlockH
//---------------------------------------------------------------------------
#include <SysUtils.hpp>
#include <Classes.hpp>
#include <SvcMgr.hpp>
#include <vcl.h>
#include <ExtCtrls.hpp>
//---------------------------------------------------------------------------
class TRemoteBlock : public TService
{
__published:    // IDE-managed Components
    void __fastcall ServiceCreate(TObject *Sender);
    void __fastcall ServiceExecute(TService *Sender);
    void __fastcall ServiceStop(TService *Sender, bool &Stopped);
    void __fastcall ServiceStart(TService *Sender, bool &Started);
private:        // User declarations
public:         // User declarations
	__fastcall TRemoteBlock(TComponent* Owner);
	TServiceController __fastcall GetServiceController(void);
    void __fastcall Block_Application(String processName);
    void __fastcall WriteLog(String txt);
    
	friend void __stdcall ServiceController(unsigned CtrlCode);
};
//---------------------------------------------------------------------------
extern PACKAGE TRemoteBlock *RemoteBlock;
//---------------------------------------------------------------------------
#endif
