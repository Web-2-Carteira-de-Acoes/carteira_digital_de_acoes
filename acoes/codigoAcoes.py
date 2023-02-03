
import array as arr 

texto = "T1LK34.SA AAPL34.SA TSMC34.SA BABA34.SA MSFT34.SA B1SA34.SA GOGL35.SA GOGL34.SA AMZO34.SA BERK34.SA H1SB34.SA UNHH34.SA TSLA34.SA JNJB34.SA EXXO34.SA VISA34.SA NVDC34.SA WALM34.SA PGCO34.SA LILY34.SA CHVX34.SA MSCD34.SA HOME34.SA M1TA34.SA N1VO34.SA PFIZ34.SA ABBV34.SA MRCK34.SA COCA34.SA PEPB34.SA ASML34.SA AVGO34.SA ORCL34.SA A1ZN34.SA TMOS34.SA COWC34.SA N1VS34.SA MCDC34.SA CSCO34.SA TMCO34.SA DHER34.SA ABTT34.SA ACNB34.SA T1MU34.SA BMYB34.SA L1IN34.SA NEXT34.SA NIKE34.SA WFCO34.SA PHMO34.SA DISB34.SA UPSS34.SA B1PP34.SA ADBE34.SA VERZ34.SA TEXA34.SA L1YG34.SA SCHW34.SA CMCS34.SA HONB34.SA RYTT34.SA MORE11.SA AMGN34.SA V1OD34.SA COPH34.SA ATTB34.SA UPAC34.SA SAPP34.SA SSFO34.SA CVSH34.SA DEEC34.SA ULEV34.SA LMTB34.SA NFLX34.SA QCOM34.SA IBMB34.SA INTU34.SA B1CS34.SA CATP34.SA LOWC34.SA ABUD34.SA E1QN34.SA RIOT34.SA BOEI34.SA H1DB34.SA P1DD34.SA SBUB34.SA ITLC34.SA SPGI34.SA ADPR34.SA AXPB34.SA GILD34.SA BLAK34.SA A1MD34.SA MDTC34.SA C1IC34.SA JDCO34.SA P1LD34.SA DEOP34.SA T1OW34.SA SNEC34.SA I1SR34.SA GEOO34.SA S1YK34.SA MDLZ34.SA JPMC34.SA TJXC34.SA B1TI34.SA R1YA34.SA A1DI34.SA A1MT34.SA CNIC34.SA M1MC34.SA MOOO34.SA BOAC34.SA ELCI34.SA NOCG34.SA REGN34.SA DUKB34.SA PYPL34.SA T1SO34.SA N1OW34.SA E1OG34.SA VALE3.SA M1RN34.SA P1GR34.SA VRTX34.SA BKNG34.SA M1UF34.SA CPRL34.SA SLBG34.SA A1PD34.SA G1SK34.SA H1CA34.SA MMMC34.SA TGTB34.SA B1SX34.SA Z1TS34.SA COLG34.SA USBC34.SA W1MC34.SA H1UM34.SA UBSG34.SA S1HW34.SA E1TN34.SA N1WG34.SA L1RC34.SA PETR3.SA PETR4.SA EQIX34.SA ATVI34.SA C1CI34.SA B1BT34.SA METB34.SA A1MX34.SA A1BB34.SA TXSA34.SA AIRB34.SA OXYP34.SA MUTC34.SA B1AM34.SA DGCO34.SA K1LA34.SA FCXO34.SA M1NS34.SA P1SA34.SA P1IO34.SA MCOR34.SA G1MI34.SA ORLY34.SA A1DM34.SA A1EP34.SA S1NP34.SA GMCO34.SA HSHY34.SA BCSA34.SA U1BE34.SA D1OM34.SA M1TT34.SA KHCB34.SA CHCM34.SA TAKP34.SA P1SX34.SA VLOE34.SA C1TA34.SA C1DN34.SA S2HO34.SA R1OP34.SA FDXB34.SA N1XP34.SA AIGB34.SA FDMO34.SA C1NC34.SA KMBB34.SA NETE34.SA E1WL34.SA AZOI34.SA MELI34.SA W1DA34.SA N1GG34.SA GSGI34.SA P1AY34.SA INGG34.SA D1EX34.SA J1CI34.SA S2NW34.SA F1TN34.SA ABEV3.SA C1TV34.SA R1SG34.SA TRVC34.SA F1NI34.SA ITUB4.SA SIMN34.SA M1SI34.SA ITUB3.SA BIIB34.SA STZB34.SA E1XC34.SA E1CL34.SA A1UT34.SA B1NT34.SA W1MB34.SA C1MG34.SA HOND34.SA R1IN34.SA ROST34.SA KMIC34.SA I1RP34.SA L1UL34.SA S1YY34.SA D1VN34.SA T1SS34.SA BIDU34.SA I1QV34.SA P1DT34.SA L1VS34.SA A1NE34.SA M1SC34.SA N1EM34.SA S2QU34.SA A1TT34.SA BONY34.SA BILB34.SA H1LT34.SA A1MB34.SA N1UE34.SA D1OW34.SA T1DG34.SA T1AM34.SA C1MI34.SA WGBA34.SA EAIN34.SA O1TI34.SA A1MP34.SA DLTR34.SA K1RC34.SA A1ME34.SA A1LN34.SA C1GP34.SA MSBR34.SA WEGE3.SA N1DA34.SA I1LM34.SA D1LR34.SA W1EL34.SA A1WK34.SA S1BS34.SA S2EA34.SA B1KR34.SA BBDC3.SA S1TT34.SA G1WW34.SA O1KE34.SA V1RS34.SA BBDC4.SA G1AR34.SA A1LB34.SA D1EL34.SA W1LT34.SA L1YB34.SA D1FS34.SA I1FF34.SA L1EN34.SA F2NV34.SA NOKI34.SA HPQB34.SA H1ZN34.SA F1AN34.SA B1AX34.SA K1EL34.SA C1BR34.SA D1DG34.SA T1RO34.SA U1RI34.SA F1EC34.SA M1TB34.SA E1FX34.SA V1MC34.SA A1RE34.SA T1SC34.SA BPAC3.SA SRXM34.SA E1QR34.SA W1YC34.SA CRIP34.SA BPAC5.SA M1KC34.SA I1QY34.SA SANB11.SA EBAY34.SA TSNF34.SA A1VB34.SA U1LT34.SA D2AS34.SA S1OU34.SA T2TD34.SA ARMT34.SA Q1UA34.SA L1CA34.SA B1MR34.SA TLNC34.SA Z1OM34.SA H1PE34.SA E1XR34.SA C1OG34.SA E1RI34.SA SANB3.SA SANB4.SA C1FI34.SA E1CO34.SA KLBN11.SA R1OL34.SA CTGP34.SA M1AA34.SA ELET6.SA P1KI34.SA G1RM34.SA ELET3.SA A1CR34.SA BBYY34.SA W1AB34.SA BBAS3.SA V1TA34.SA NUBR33.SA E1XP34.SA W1MG34.SA S2UI34.SA M1RO34.SA C1PB34.SA MKLC34.SA P2IN34.SA FOXC34.SA FSLR34.SA T1TW34.SA R2BL34.SA CINF34.SA E2TS34.SA S1YF34.SA ITSA4.SA A1TH34.SA ARNC34.SA L1YV34.SA O1MC34.SA P1KX34.SA ITSA3.SA F1MC34.SA K1EY34.SA A1LG34.SA N1VR34.SA MOSC34.SA H2UB34.SA S1PO34.SA M1LC34.SA I1RM34.SA BPAC11.SA L1DO34.SA M1GM34.SA S1PL34.SA E1SS34.SA A1PA34.SA A1KA34.SA R1CL34.SA B3SA3.SA K1IM34.SA P2LT34.SA P1EA34.SA M1DB34.SA T1CH34.SA C1BO34.SA Z1BR34.SA F1RA34.SA D2PZ34.SA U1AL34.SA S1IV34.SA B2HI34.SA H1ST34.SA BBSE3.SA C2PT34.SA SUZB3.SA VIVT3.SA S1TX34.SA M1AS34.SA C1SU34.SA G2DD34.SA PHGN34.SA N1BI34.SA M1TC34.SA U2ST34.SA C1HR34.SA C1BS34.SA NMRH34.SA S1WK34.SA S1NN34.SA C1NS34.SA O1KT34.SA R1EG34.SA S1RP34.SA D1OC34.SA C1CL34.SA P1HM34.SA BOXP34.SA W1DC34.SA T1EV34.SA H1FC34.SA RDOR3.SA VFCO34.SA U1HS34.SA RENT3.SA W1SO34.SA M1KT34.SA A1EG34.SA H1II34.SA GGBR3.SA GGBR4.SA G1FI34.SA FMSC34.SA S2TO34.SA T1WL34.SA TPRY34.SA A1OS34.SA L1BT34.SA D1IS34.SA JBSS3.SA B1IL34.SA F1FI34.SA V1IP34.SA XPBR31.SA I1VZ34.SA A1AP34.SA S1KM34.SA J1EF34.SA AALL34.SA C2OI34.SA A1UA34.SA S1EA34.SA CAPH34.SA RADL3.SA SBSP3.SA N1RG34.SA P2AT34.SA K1TC34.SA CPFE3.SA COTY34.SA P2LN34.SA TAEE11.SA M2PW34.SA M1HK34.SA DVAI34.SA H1RB34.SA RAIL3.SA HAPV3.SA E1DU34.SA WABC34.SA CRFB3.SA USSX34.SA CSAN3.SA R1KU34.SA C1OU34.SA EGIE3.SA PRIO3.SA E2ST34.SA T2PX34.SA TIMS3.SA EQTL3.SA MACY34.SA T1AL34.SA CMIG4.SA N1WL34.SA L1MN34.SA WUNI34.SA CMIG3.SA HYPE3.SA T1EC34.SA ASAI3.SA W1IX34.SA A1IV34.SA P2EN34.SA D2KN34.SA W1BO34.SA CXSE3.SA E2EF34.SA P1VH34.SA V1NO34.SA T2DH34.SA U1AI34.SA L1EG34.SA GOLL4.SA CMIN3.SA KLBN3.SA CCRO3.SA KLBN4.SA C1AB34.SA LREN3.SA W2YF34.SA CPLE3.SA ENGI4.SA I1AC34.SA CSNA3.SA CPLE6.SA MGLU3.SA BRKM5.SA ENGI3.SA CPLE5.SA A1YX34.SA ENEV3.SA BRKM3.SA NEOE3.SA ENMT4.SA ENMT3.SA VBBR3.SA TOTS3.SA RIGG34.SA TRPL4.SA TRPL3.SA CGAS5.SA CGAS3.SA NTCO3.SA ALUP11.SA STOC31.SA EQPA3.SA K1SS34.SA AURE3.SA EQPA7.SA GOAU3.SA PSSA3.SA GOAU4.SA A2MC34.SA UGPA3.SA T1RI34.SA PAGS34.SA XRXB34.SA CIEL3.SA GMAT3.SA MDIA3.SA MULT3.SA VAMO3.SA REDE3.SA ENGI11.SA H1BI34.SA TAEE3.SA TAEE4.SA ENBR3.SA BRAP3.SA S1LG34.SA BRAP4.SA EMBR3.SA K2CG34.SA MRSA5B.SA A1LL34.SA INTB3.SA CEEB3.SA ALPA4.SA SLCE3.SA UNIP6.SA UNIP3.SA ALUP4.SA ALPA3.SA USIM3.SA ARZZ3.SA UNIP5.SA SULA11.SA USIM5.SA SMTO3.SA RECV3.SA AMER3.SA SMFT3.SA BRFS3.SA SOMA3.SA ALUP3.SA BEEF3.SA GGPS3.SA DASA3.SA U2PW34.SA WHRL3.SA WHRL4.SA BPAN4.SA BNBR3.SA EKTR4.SA EKTR3.SA BRML3.SA RRRP3.SA STBP3.SA CBAV3.SA BSLI4.SA GRND3.SA DXCO3.SA CSMG3.SA F1SL34.SA F2VR34.SA AESB3.SA MOAR3.SA FLRY3.SA BSLI3.SA SIMH3.SA MEGA3.SA SAPR4.SA SAPR3.SA CYRE3.SA VIVA3.SA VVEO3.SA PCAR3.SA ODPV3.SA FESA4.SA BLAU3.SA LWSA3.SA PORT3.SA MRFG3.SA SULA3.SA GETT3.SA ALSO3.SA VGIR11.SA SULA4.SA GETT4.SA TTEN3.SA B2YN34.SA SAPR11.SA ABCB4.SA BRSR6.SA BRSR3.SA EQMA3B.SA INBR32.SA GPRO34.SA KNCR11.SA VIIA3.SA BRSR5.SA COGN3.SA TUPY3.SA BOAS3.SA MRVE3.SA AZUL4.SA ARML3.SA LEVE3.SA CSRN3.SA CSRN5.SA GPAR3.SA CURY3.SA HGLG11.SA JHSF3.SA GUAR3.SA LOGN3.SA ONCO3.SA V2ME34.SA CBEE3.SA ENAT3.SA PETZ3.SA IGTI3.SA SBFG3.SA EZTC3.SA VULC3.SA ECOR3.SA CAML3.SA YDUQ3.SA MOVI3.SA BRPR3.SA MLAS3.SA RAPT3.SA POMO3.SA AGRO3.SA RAPT4.SA FRAS3.SA POMO4.SA CEED3.SA CEED4.SA XPLG11.SA PARD3.SA MILS3.SA LAND3.SA AALR3.SA ORVR3.SA GEPA3.SA GEPA4.SA MATD3.SA AMBP3.SA JALL3.SA AURA33.SA DIRR3.SA KNRI11.SA CLSC4.SA RECR11.SA BTLG11.SA IRBR3.SA RANI3.SA BEES4.SA MYPK3.SA VITT3.SA BEES3.SA LIGT3.SA VISC11.SA KEPL3.SA PGMN3.SA HBSA3.SA TASA3.SA QUAL3.SA TASA4.SA JSLG3.SA LOGG3.SA HFOF11.SA TFCO4.SA BRCR11.SA ANIM3.SA CSED3.SA BAZA3.SA PNVL3.SA MODL3.SA JSRE11.SA HGRE11.SA AGXY3.SA ZAMP3.SA ELMD3.SA BBPO11.SA TGMA3.SA BMGB4.SA FIQE3.SA SQIA3.SA HSML11.SA OIBR3.SA HGCR11.SA BMOB3.SA WIZS3.SA EMAE4.SA CVCB3.SA ROMI3.SA SOJA3.SA BRIT3.SA COCE5.SA OIBR4.SA OFSA3.SA HGBS11.SA POSI3.SA CASH3.SA PTBL3.SA CRPG6.SA CRPG5.SA BMEB3.SA EVEN3.SA BMEB4.SA CLSA3.SA SCAR3.SA FHER3.SA IFCM3.SA DMMO3.SA SHUL4.SA TELB4.SA VRTA11.SA LAVV3.SA KRSA3.SA ABCP11.SA SHPH11.SA TELB3.SA GTLG11.SA LJQQ3.SA EUCA3.SA WLMM4.SA BRIV3.SA DESK3.SA RBRX11.SA AERI3.SA BRIV4.SA CEBR3.SA MALL11.SA RBRF11.SA VLID3.SA EUCA4.SA CEBR5.SA PLPL3.SA MEAL3.SA BRGE8.SA BRGE11.SA BRGE3.SA CEBR6.SA IRDM11.SA DEXP4.SA CEAB3.SA KNSC11.SA DEXP3.SA MELK3.SA PEAB4.SA ETER3.SA PEAB3.SA PEAB3.SA TRIS3.SA DOHL4.SA OPCT3.SA RPAD3.SA TRAD3.SA RPAD6.SA BCRI11.SA AFLT3.SA SDIL11.SA SEER3.SA CGRA4.SA RBRL11.SA CGRA3.SA CRIV3.SA ALLD3.SA APER3.SA CRIV4.SA BCFF11.SA MTSA4.SA ESPA3.SA PQDP11.SA CSUD3.SA SEQL3.SA MDNE3.SA RNEW4.SA RNEW3.SA BIOM3.SA HBRE3.SA TEND3.SA MXRF11.SA PFRM3.SA AMAR3.SA NVHO11.SA RNEW11.SA MTRE3.SA MFII11.SA HABT11.SA FCFL11.SA MFCR11.SA CARE11.SA RBVA11.SA LVTC3.SA PTNT4.SA NGRD3.SA ALPK3.SA PTNT3.SA BGIP3.SA BGIP4.SA PORD11.SA CSAB4.SA FIIB11.SA BCIA11.SA MBLY3.SA HBOR3.SA RDNI3.SA G2DI33.SA BAHI3.SA LPSB3.SA CAMB3.SA BBFI11B.SA GFSA3.SA PRNR3.SA GPIV33.SA QAGR11.SA PDTC3.SA JOPA3.SA LUXM4.SA PPLA11.SA TCSA3.SA ENJU3.SA INEP3.SA DMVF3.SA INEP4.SA JASC11.SA PMAM3.SA HBTS5.SA PLCR11.SA VLOL11.SA BPFF11.SA TPIS3.SA AHEB3.SA AHEB6.SA RSUL4.SA UCAS3.SA EALT4.SA FLMA11.SA DOTZ3.SA TECN3.SA EALT3.SA CXAG11.SA CXCI11.SA ONEF11.SA EPAR3.SA AVLL3.SA SHOW3.SA BBRC11.SA BOBR4.SA NINJ3.SA VCRR11.SA BLCA11.SA RNGO11.SA FIGS11.SA BMKS3.SA WEST3.SA CTNM4.SA CTNM3.SA PRSN11B.SA MGCR11.SA PLAS3.SA LLIS3.SA LUPA3.SA RPMG3.SA BMLC11.SA BALM3.SA BALM4.SA AZEV4.SA AZEV3.SA FPAB11.SA MNDL3.SA SNCI11.SA CEOC11.SA HUCG11.SA CTKA3.SA CTKA4.SA FAED11.SA GCRI11.SA BMIN4.SA PINE4.SA RBED11.SA EURO11.SA OURE11.SA BNFS11.SA SGPS3.SA VIVR3.SA CBOP11.SA DVFF11.SA RBRS11.SA FAMB11B.SA MGHT11.SA SPTW11.SA ITIT11.SA CXCE11B.SA RBRD11.SA RBOP11.SA JFEN3.SA CTSA4.SA CTSA3.SA ATOM3.SA CEDO4.SA ROOF11.SA RSID3.SA DTCY3.SA FATN11.SA MGEL4.SA EDFO11B.SA DRIT11B.SA BIME11.SA MNPR3.SA RCSL4.SA RCSL3.SA NEXP3.SA IGBR3.SA APTO11.SA XPCM11.SA PDGR3.SA MWET4.SA BLMC11.SA FIVN11.SA TXRX4.SA CTXT11.SA CALI3.SA SLED4.SA SLED3.SA SNSY5.SA ATMP3.SA SNSY3.SA FMOF11.SA PRSV11.SA NORD3.SA HAGA4.SA SCPF11.SA GCFF11.SA PLRI11.SA OSXB3.SA HAGA3.SA CXTL11.SA PABY11.SA RNDP11.SA BDLL3.SA BDLL4.SA HOOT4.SA TEKA4.SA RBVO11.SA FRTA3.SA HETA4.SA RBDS11.SA PNPR11.SA GRMZ5L.SA FSTU11.SA EQPA7F.SA HBCR11.SA COCE3F.SA SRVD11.SA PEVC11.SA ENMT3F.SA ESTR4F.SA JOPA3F.SA C2CA34.SA E2LS34.SA F2RT34.SA N2VC34.SA L2AZ34.SA RBHY12.SA BCWV39.SA BVLU39.SA BEFV39.SA FZDA11.SA TF495.SA ZIFI11.SA TF545.SA TF525.SA TF693.SA TF573.SA TF703.SA TF473.SA TF685.SA BDLL4F.SA BPAR3F.SA BAAX39.SA G1DS34.SA BREV11.SA FPOR11.SA BUTL39.SA SNSY5F.SA BEWW39.SA BAHI3F.SA CJCT11.SA LASC11.SA RBIR11.SA CBEE3F.SA U2PS34.SA BSOX39.SA BIOM3F.SA HGIC11.SA REIT11.SA PEAB3F.SA RSUL4F.SA RPAD3F.SA BSIL39.SA BIJH39.SA EQMA3BF.SA BIYE39.SA EMAE4F.SA MNPR3F.SA BIVE39.SA AGXY3F.SA BIDB11.SA LUXM4F.SA IFCM3F.SA IGBR3F.SA BMIL39.SA GOVE11.SA ESGD11.SA CRIV3F.SA JRDM11.SA BIVW39.SA NORD3F.SA TFCO4F.SA W1BD34.SA FLCR11.SA BEDC39.SA BHYG39.SA BGRT39.SA H2TA34.SA BOTZ39.SA BLPX39.SA MERC4F.SA EKTR3F.SA USAL11.SA HAGA4F.SA OFSA3F.SA HCRI11.SA BURA39.SA EQPA3F.SA IRFM11.SA NEWU11.SA PNVL3F.SA LLIS3F.SA CGRA4F.SA SLED4F.SA USDB11.SA BACW39.SA AGRI11.SA PDTC3F.SA POSI3F.SA BITH11.SA CLSA3F.SA CRPT11.SA TIMS3F.SA BAZA3F.SA NEWU11.SA BMEB4F.SA ENGI3F.SA BITI11.SA BTLT39.SA SEQL3F.SA ETER3F.SA MLAS3F.SA HCRI11.SA SHOT11.SA MDIA3F.SA CEBR6F.SA IRFM11.SA QDFI11.SA QAMI11.SA ATMP3F.SA PORT3F.SA OFSA3F.SA BURA39.SA GFSA1.SA BITH11.SA ALUP3F.SA CLSA3F.SA ESGD11.SA GFSA1F.SA PNVL3F.SA HTMX11.SA TFCO4F.SA LLIS3F.SA LEVE3F.SA SOJA3F.SA RBRY11.SA NASD11.SA SAPR4F.SA GRND3F.SA CASH3F.SA ELET3F.SA CURY3F.SA COGN3F.SA AGRX11.SA GGPS3F.SA MEAL3F.SA BRIV3F.SA BBAS3F.SA FGAA11.SA POSI3F.SA ARCT11.SA VIIA3F.SA HCTR11.SA TAEE11F.SA VIVT3F.SA BAAX39.SA ENEV3F.SA FLRY3F.SA PDGR3F.SA SUZB3F.SA YDRO11.SA PSSA3F.SA BMOB3F.SA XFIX11.SA ALUP11F.SA VOTS11.SA MULT3F.SA BOVV11.SA JHSF3F.SA BRML3F.SA CSNA3F.SA TIMS3F.SA USDB11.SA REDE3F.SA KNIP11.SA ENBR3F.SA KNHY11.SA VIVA3F.SA XPML11.SA VIFI11.SA XINA11.SA OUJP11.SA KIVO11.SA JSLG3F.SA MNPR3F.SA VITT3F.SA CPLE6F.SA VLID3F.SA SPXI11.SA CSUD3F.SA RANI3F.SA POMO4F.SA PETR3F.SA SAPR3F.SA PFIN11.SA SHOW3F.SA SARE11.SA ARRI11.SA VVEO3F.SA LAVV3F.SA PTBL3F.SA BOVA11.SA GGRC11.SA VIFI11.SA XINA11.SA KIVO11.SA ARCT11.SA FGAA11.SA BBAS3F.SA RCFF11.SA ENMT4F.SA FRIO3F.SA TXRX3F.SA EQPA5F.SA BLUR11.SA CRPG3F.SA CASN3F.SA HDEL11.SA SLED3F.SA FLRP11.SA C2OL34.SA S2FM34.SA A2SO34.SA M2RT34.SA BIYC39.SA ZAVI11.SA WSEC11.SA MOAR3F.SA BAER39.SA BIEU39.SA HOOT4F.SA CXRI11.SA Q2SC34.SA BEWJ39.SA BEWY39.SA BIWF39.SA BEWT39.SA BEWQ39.SA BSDV39.SA EXES11.SA IMBB11.SA EQPA6F.SA MCHY11.SA N2TN34.SA M2PR34.SA ODER4F.SA O2NS34.SA RMAI11.SA A2RE34.SA HOSI11.SA C2RW34.SA XPHT11.SA TF665.SA TF713.SA TF485.SA TF535.SA TF515.SA TF519.SA V2MW34.SA TF505.SA TF585.SA BKSA39.SA M2RV34.SA SCVB11.SA CSRN6F.SA BSLV39.SA WEB311.SA BMEB3F.SA ENDD11.SA KNOX11.SA BICR11.SA BEEM39.SA BDRI39.SA RNEW2.SA RBIF11.SA FIXA11.SA RNEW1F.SA RNEW11F.SA RCFA11.SA FESA3F.SA OGIN11.SA HAGA3F.SA BRSR5F.SA TRIG11.SA CEDO3F.SA BALM4F.SA CBAV3F.SA EQTL3F.SA URET11.SA DMVF3F.SA LREN3F.SA MGFF11.SA ROMI3F.SA TRPL4F.SA SANB11F.SA IFRA11.SA BLAU3F.SA FNAM11.SA RNEW1.SA EZTC3F.SA BLMR11.SA TASA3F.SA MILS3F.SA BMTU39.SA PFRM3F.SA BTAG11.SA RCSL4F.SA JFLL11.SA DESK3F.SA ONCO3F.SA ECOR3F.SA IDFI11.SA GPAR3F.SA E2NP34.SA AZEV4F.SA CRPG6F.SA BIEM39.SA ATSA11.SA RSID3F.SA GENB11.SA PATC11.SA RNEW2F.SA BRBI11F.SA RDPD11.SA TASA3F.SA MILS3F.SA WHRL4F.SA OSXB3F.SA USTK11.SA INTB3F.SA MYPK3F.SA CMIG3F.SA ITUB3F.SA MWET4F.SA MILL11.SA ALSO3F.SA HSLG11.SA SVAL11.SA EMBR3F.SA ANIM3F.SA BIEF39.SA RADL3F.SA QBTC11.SA URET11.SA DMVF3F.SA SANB11F.SA IFRA11.SA CBAV3F.SA PATL11.SA BOVB11.SA WRLD11.SA BDIF11.SA MODL3F.SA GFSA3F.SA ATOM3F.SA JPPA11.SA AESB1F.SA GOLD11.SA OPCT3F.SA LREN3F.SA ROMI3F.SA TRPL4F.SA MGFF11.SA TGAR11.SA LVBI11.SA TTEN3F.SA MCHF11.SA RAIZ4.SA ARML3F.SA BOVX11.SA EZTC3F.SA EQTL3F.SA BLMR11.SA NEOE3F.SA BLAU3F.SA CIEL3F.SA BPAC11F.SA DIVO11.SA SNAG11.SA SANB3F.SA GTWR11.SA LPSB3F.SA KFOF11.SA BTCI11.SA CPLE3F.SA CMIN3F.SA BRKM5F.SA VULC3F.SA CXSE3F.SA ENGI11F.SA FNAM11.SA VSLH11.SA RBRP11.SA ITSA3F.SA MOVI3F.SA VAMO3F.SA RCRB11.SA VIVR3F.SA AERI3F.SA CPLE11.SA BBDC3F.SA HGFF11.SA FESA4F.SA QBTC11.SA BTCI11.SA CPLE3F.SA BRKM5F.SA PGMN3F.SA ODPV3F.SA CYCR11.SA PVBI11.SA VXXV11.SA ABGD39.SA NUTR3F.SA ERPA11.SA MNHT5L.SA PATI3F.SA TKNO4F.SA ESTR3F.SA TSER11.SA BKYY39.SA HCRA11.SA AHEB3F.SA ESUT11F.SA CSRN5F.SA CSAB4F.SA AVLL3F.SA DTCY3F.SA CEED4F.SA S2WA34.SA Z2SC34.SA BIXG39.SA BXTC39.SA BSUS39.SA WTSP11B.SA ELET5F.SA FSRF11.SA BURT39.SA BSHY39.SA BIYF39.SA BBCN39.SA B5MB11.SA BKCH39.SA TF513.SA TF681.SA TF503.SA TF675.SA T2ER34.SA TF563.SA TF543.SA BKXI39.SA A2MB34.SA E1DI34.SA BXPO11.SA S2NA34.SA PTNT3F.SA ESGU11.SA L2PL34.SA EPAR3F.SA BIXJ39.SA HSRE11.SA PEMA11.SA S2TA34.SA WLMM3F.SA SMAB11.SA XPHT12.SA BBOV11.SA FSPE11F.SA META11.SA DEBB11.SA S2TW34.SA XBOV11.SA RECX11.SA HTEK11.SA HUSC11.SA P2AN34.SA USIM6F.SA NFTS11.SA ISUS11.SA NINJ3F.SA BDVD39.SA BEWL39.SA CALI3F.SA CEEB3F.SA CPTI11.SA BHEF39.SA CORN11.SA DEXP3F.SA BOBR4F.SA BDIV11.SA ESGB11.SA BBUG39.SA FSRF11F.SA LOGN3F.SA MFAI11.SA RFOF11.SA ACWI11.SA GMAT3F.SA L2RN34.SA MAPT4F.SA CLSC3F.SA UGPA3F.SA BEWG39.SA USIM3F.SA MTRE3F.SA TUPY3F.SA WEST3F.SA BRKM6F.SA INEP4F.SA DEXP3F.SA 5GTK11.SA BEWL39.SA CALI3F.SA BOBR4F.SA TRAD3F.SA JFEN3F.SA XMAL11.SA UNIP5F.SA SCAR3F.SA GETT4F.SA RFOF11.SA CPTI11.SA FSRF11F.SA L2RN34.SA MAPT4F.SA CEEB3F.SA CLSC3F.SA IRIM11.SA NFTS11.SA ISUS11.SA ESGB11.SA LOGN3F.SA BIJR39.SA BBGO11.SA UGPA3F.SA FVPQ11.SA VSHO11.SA OIAG11.SA CRFB3F.SA MATB11.SA SULA4F.SA IGTI11F.SA ENJU3F.SA CEBR3F.SA DAMT11B.SA CTSA4F.SA BOAS3F.SA GGBR3F.SA TPIS3F.SA VCRI11.SA BLQD39.SA RNEW12F.SA STBP3F.SA RECX11.SA YDUQ3F.SA SMFT3F.SA ITUB4F.SA XPPR11.SA TAEE3F.SA VGHF11.SA MORC11.SA CACR11.SA VCJR11.SA CMIG4F.SA ESPA3F.SA ITSA4F.SA PICE11.SA NTCO3F.SA NINJ3F.SA XPSF11.SA CORN11.SA ACWI11.SA OULG11.SA ALPA4F.SA TEPP11.SA BEWG39.SA MRFG3F.SA TOTS3F.SA BDVD39.SA IRBR3F.SA BEES4F.SA UNIP3F.SA CPTR11.SA SPXB11.SA BDIV11.SA ALUP4F.SA VGIP11.SA AURE3F.SA AFHI11.SA JSAF11.SA GOLL4F.SA XPCA11.SA XPID11.SA KISU11.SA LOGG3F.SA BARI11.SA BBSE3F.SA ABEV3F.SA UNIP6F.SA GGBR4F.SA AZUL4F.SA VTLT11.SA HASH11.SA IGTI11F.SA CLSC4F.SA BRKM6F.SA TAEE3F.SA XPPR11.SA MORC11.SA VGHF11.SA CACR11.SA SULA4F.SA XPSF11.SA BGIP3F.SA CEEB5F.SA BRGE11F.SA DMFN3F.SA LIPR3F.SA CCME11.SA BQCL39.SA CEDO4F.SA F2IC34.SA F2IV34.SA GEPA3F.SA TEKA3F.SA F2RS34.SA BEWP39.SA HAAA11.SA AHEB5F.SA VSEC11.SA BZRO39.SA BRLA11.SA CTKA4F.SA BFXI39.SA BICL39.SA I2RS34.SA J2AZ34.SA WLMM4F.SA BRIV4F.SA BDOM11.SA BQUA39.SA TF523.SA TF493.SA TF655.SA TF623.SA A2XO34.SA BEWU39.SA TF553.SA TF593.SA FPNG11.SA BIBB39.SA IBOB11.SA BDVY39.SA TRNT11.SA NAVT11.SA SIVR39.SA PSVM11F.SA BICE11.SA S2CH34.SA BGIP4F.SA TXRX4F.SA BGNO39.SA BPFV39.SA BLPA39.SA BPVE39.SA BFNX39.SA EUCA3F.SA RBLG11.SA BSCZ39.SA PLCA11.SA CTNM4F.SA PEAB4F.SA BCLO39.SA BCHQ39.SA EKTR4F.SA FSTU11F.SA NEXP3F.SA RCSL3F.SA GDXB39.SA HGAG11.SA DESK1F.SA GURU11.SA CPLE5F.SA GETT3F.SA KCRE11.SA TGMA3F.SA CTNM3F.SA CPFF11.SA O2HI34.SA LUGG11.SA ITIP11.SA HBSA3F.SA ALMI11.SA PINE4F.SA BSLI4F.SA BRAX11.SA BSLI3F.SA CSRN3F.SA BIEV39.SA HPDP11.SA ALLD3F.SA BEWZ39.SA BBOI11.SA TECN3F.SA DASA3F.SA GEPA4F.SA LJQQ3F.SA ITIP11.SA HGAG11.SA XPIE11.SA BIEI39.SA CSED3F.SA RCSL3F.SA EUCA4F.SA ESGE11.SA FIQE3F.SA FNOR11.SA TEND3F.SA BEWC39.SA BUSR39.SA CCRF11.SA AFLT3F.SA BIXN39.SA BRSR3F.SA HSAF11.SA HGPO11.SA FHER3F.SA HBSA3F.SA GDXB39.SA L2SI34.SA GUAR3F.SA CPLE5F.SA O2HI34.SA LUGG11.SA ENGI4F.SA BEES3F.SA MEGA3F.SA KINP11.SA LAND3F.SA ALLD3F.SA DESK1F.SA LIGT3F.SA INEP3F.SA NCHB11.SA LGCP11.SA NEWL11.SA ARZZ3F.SA PCAR3F.SA PLPL3F.SA NGRD3F.SA CPFF11.SA KCRE11.SA AESB1.SA BRBI11.SA SEER3F.SA SAPR11F.SA RURA11.SA CSMG3F.SA GETT3F.SA CYRE3F.SA GOAU4F.SA TAEE4F.SA AGRO3F.SA ETHE11.SA SHUL4F.SA REVE11.SA PETZ3F.SA IGTI11.SA DEVA11.SA BRCO11.SA SMAL11.SA BRAP4F.SA KEPL3F.SA XPIN11.SA GALG11.SA JURO11.SA MCCI11.SA RZAG11.SA AIEC11.SA SOMA3F.SA SMTO3F.SA CXCO11.SA CSAN3F.SA TORD11.SA VILG11.SA EGIE3F.SA BTRA11.SA RAIZ4F.SA RZAK11.SA IVVB11.SA CCRO3F.SA RECV3F.SA SQIA3F.SA SMAC11.SA TRXF11.SA SIMH3F.SA EVEN3F.SA ELET6F.SA CVCB3F.SA BBFO11.SA HAPV3F.SA B3SA3F.SA MRVE3F.SA"

textoArray = 'T1LK34.SA','AAPL34.SA','TSMC34.SA','BABA34.SA','MSFT34.SA','B1SA34.SA','GOGL35.SA','GOGL34.SA','AMZO34.SA','BERK34.SA','H1SB34.SA','UNHH34.SA','TSLA34.SA','JNJB34.SA','EXXO34.SA','VISA34.SA','NVDC34.SA','WALM34.SA','PGCO34.SA','LILY34.SA','CHVX34.SA','MSCD34.SA','HOME34.SA','M1TA34.SA','N1VO34.SA','PFIZ34.SA','ABBV34.SA','MRCK34.SA','COCA34.SA','PEPB34.SA','ASML34.SA','AVGO34.SA','ORCL34.SA','A1ZN34.SA','TMOS34.SA','COWC34.SA','N1VS34.SA','MCDC34.SA','CSCO34.SA','TMCO34.SA','DHER34.SA','ABTT34.SA','ACNB34.SA','T1MU34.SA','BMYB34.SA','L1IN34.SA','NEXT34.SA','NIKE34.SA','WFCO34.SA','PHMO34.SA','DISB34.SA','UPSS34.SA','B1PP34.SA','ADBE34.SA','VERZ34.SA','TEXA34.SA','L1YG34.SA','SCHW34.SA','CMCS34.SA','HONB34.SA','RYTT34.SA','MORE11.SA','AMGN34.SA','V1OD34.SA','COPH34.SA','ATTB34.SA','UPAC34.SA','SAPP34.SA','SSFO34.SA','CVSH34.SA','DEEC34.SA','ULEV34.SA','LMTB34.SA','NFLX34.SA','QCOM34.SA','IBMB34.SA','INTU34.SA','B1CS34.SA','CATP34.SA','LOWC34.SA','ABUD34.SA','E1QN34.SA','RIOT34.SA','BOEI34.SA','H1DB34.SA','P1DD34.SA','SBUB34.SA','ITLC34.SA','SPGI34.SA','ADPR34.SA','AXPB34.SA','GILD34.SA','BLAK34.SA','A1MD34.SA','MDTC34.SA','C1IC34.SA','JDCO34.SA','P1LD34.SA','DEOP34.SA','T1OW34.SA','SNEC34.SA','I1SR34.SA','GEOO34.SA','S1YK34.SA','MDLZ34.SA','JPMC34.SA','TJXC34.SA','B1TI34.SA','R1YA34.SA','A1DI34.SA','A1MT34.SA','CNIC34.SA','M1MC34.SA','MOOO34.SA','BOAC34.SA','ELCI34.SA','NOCG34.SA','REGN34.SA','DUKB34.SA','PYPL34.SA','T1SO34.SA','N1OW34.SA','E1OG34.SA','VALE3.SA','M1RN34.SA','P1GR34.SA','VRTX34.SA','BKNG34.SA','M1UF34.SA','CPRL34.SA','SLBG34.SA','A1PD34.SA','G1SK34.SA','H1CA34.SA','MMMC34.SA','TGTB34.SA','B1SX34.SA','Z1TS34.SA','COLG34.SA','USBC34.SA','W1MC34.SA','H1UM34.SA','UBSG34.SA','S1HW34.SA','E1TN34.SA','N1WG34.SA','L1RC34.SA','PETR3.SA','PETR4.SA','EQIX34.SA','ATVI34.SA','C1CI34.SA','B1BT34.SA','METB34.SA','A1MX34.SA','A1BB34.SA','TXSA34.SA','AIRB34.SA','OXYP34.SA','MUTC34.SA','B1AM34.SA','DGCO34.SA','K1LA34.SA','FCXO34.SA','M1NS34.SA','P1SA34.SA','P1IO34.SA','MCOR34.SA','G1MI34.SA','ORLY34.SA','A1DM34.SA','A1EP34.SA','S1NP34.SA','GMCO34.SA','HSHY34.SA','BCSA34.SA','U1BE34.SA','D1OM34.SA','M1TT34.SA','KHCB34.SA','CHCM34.SA','TAKP34.SA','P1SX34.SA','VLOE34.SA','C1TA34.SA','C1DN34.SA','S2HO34.SA','R1OP34.SA','FDXB34.SA','N1XP34.SA','AIGB34.SA','FDMO34.SA','C1NC34.SA','KMBB34.SA','NETE34.SA','E1WL34.SA','AZOI34.SA','MELI34.SA','W1DA34.SA','N1GG34.SA','GSGI34.SA','P1AY34.SA','INGG34.SA','D1EX34.SA','J1CI34.SA','S2NW34.SA','F1TN34.SA','ABEV3.SA','C1TV34.SA','R1SG34.SA','TRVC34.SA','F1NI34.SA','ITUB4.SA','SIMN34.SA','M1SI34.SA','ITUB3.SA','BIIB34.SA','STZB34.SA','E1XC34.SA','E1CL34.SA','A1UT34.SA','B1NT34.SA','W1MB34.SA','C1MG34.SA','HOND34.SA','R1IN34.SA','ROST34.SA','KMIC34.SA','I1RP34.SA','L1UL34.SA','S1YY34.SA','D1VN34.SA','T1SS34.SA','BIDU34.SA','I1QV34.SA','P1DT34.SA','L1VS34.SA','A1NE34.SA','M1SC34.SA','N1EM34.SA','S2QU34.SA','A1TT34.SA','BONY34.SA','BILB34.SA','H1LT34.SA','A1MB34.SA','N1UE34.SA','D1OW34.SA','T1DG34.SA','T1AM34.SA','C1MI34.SA','WGBA34.SA','EAIN34.SA','O1TI34.SA','A1MP34.SA','DLTR34.SA','K1RC34.SA','A1ME34.SA','A1LN34.SA','C1GP34.SA','MSBR34.SA','WEGE3.SA','N1DA34.SA','I1LM34.SA','D1LR34.SA','W1EL34.SA','A1WK34.SA','S1BS34.SA','S2EA34.SA','B1KR34.SA','BBDC3.SA','S1TT34.SA','G1WW34.SA','O1KE34.SA','V1RS34.SA','BBDC4.SA','G1AR34.SA','A1LB34.SA','D1EL34.SA','W1LT34.SA','L1YB34.SA','D1FS34.SA','I1FF34.SA','L1EN34.SA','F2NV34.SA','NOKI34.SA','HPQB34.SA','H1ZN34.SA','F1AN34.SA','B1AX34.SA','K1EL34.SA','C1BR34.SA','D1DG34.SA','T1RO34.SA','U1RI34.SA','F1EC34.SA','M1TB34.SA','E1FX34.SA','V1MC34.SA','A1RE34.SA','T1SC34.SA','BPAC3.SA','SRXM34.SA','E1QR34.SA','W1YC34.SA','CRIP34.SA','BPAC5.SA','M1KC34.SA','I1QY34.SA','SANB11.SA','EBAY34.SA','TSNF34.SA','A1VB34.SA','U1LT34.SA','D2AS34.SA','S1OU34.SA','T2TD34.SA','ARMT34.SA','Q1UA34.SA','L1CA34.SA','B1MR34.SA','TLNC34.SA','Z1OM34.SA','H1PE34.SA','E1XR34.SA','C1OG34.SA','E1RI34.SA','SANB3.SA','SANB4.SA','C1FI34.SA','E1CO34.SA','KLBN11.SA','R1OL34.SA','CTGP34.SA','M1AA34.SA','ELET6.SA','P1KI34.SA','G1RM34.SA','ELET3.SA','A1CR34.SA','BBYY34.SA','W1AB34.SA','BBAS3.SA','V1TA34.SA','NUBR33.SA','E1XP34.SA','W1MG34.SA','S2UI34.SA','M1RO34.SA','C1PB34.SA','MKLC34.SA','P2IN34.SA','FOXC34.SA','FSLR34.SA','T1TW34.SA','R2BL34.SA','CINF34.SA','E2TS34.SA','S1YF34.SA','ITSA4.SA','A1TH34.SA','ARNC34.SA','L1YV34.SA','O1MC34.SA','P1KX34.SA','ITSA3.SA','F1MC34.SA','K1EY34.SA','A1LG34.SA','N1VR34.SA','MOSC34.SA','H2UB34.SA','S1PO34.SA','M1LC34.SA','I1RM34.SA','BPAC11.SA','L1DO34.SA','M1GM34.SA','S1PL34.SA','E1SS34.SA','A1PA34.SA','A1KA34.SA','R1CL34.SA','B3SA3.SA','K1IM34.SA','P2LT34.SA','P1EA34.SA','M1DB34.SA','T1CH34.SA','C1BO34.SA','Z1BR34.SA','F1RA34.SA','D2PZ34.SA','U1AL34.SA','S1IV34.SA','B2HI34.SA','H1ST34.SA','BBSE3.SA','C2PT34.SA','SUZB3.SA','VIVT3.SA','S1TX34.SA','M1AS34.SA','C1SU34.SA','G2DD34.SA','PHGN34.SA','N1BI34.SA','M1TC34.SA','U2ST34.SA','C1HR34.SA','C1BS34.SA','NMRH34.SA','S1WK34.SA','S1NN34.SA','C1NS34.SA','O1KT34.SA','R1EG34.SA','S1RP34.SA','D1OC34.SA','C1CL34.SA','P1HM34.SA','BOXP34.SA','W1DC34.SA','T1EV34.SA','H1FC34.SA','RDOR3.SA','VFCO34.SA','U1HS34.SA','RENT3.SA','W1SO34.SA','M1KT34.SA','A1EG34.SA','H1II34.SA','GGBR3.SA','GGBR4.SA','G1FI34.SA','FMSC34.SA','S2TO34.SA','T1WL34.SA','TPRY34.SA','A1OS34.SA','L1BT34.SA','D1IS34.SA','JBSS3.SA','B1IL34.SA','F1FI34.SA','V1IP34.SA','XPBR31.SA','I1VZ34.SA','A1AP34.SA','S1KM34.SA','J1EF34.SA','AALL34.SA','C2OI34.SA','A1UA34.SA','S1EA34.SA','CAPH34.SA','RADL3.SA','SBSP3.SA','N1RG34.SA','P2AT34.SA','K1TC34.SA','CPFE3.SA','COTY34.SA','P2LN34.SA','TAEE11.SA','M2PW34.SA','M1HK34.SA','DVAI34.SA','H1RB34.SA','RAIL3.SA','HAPV3.SA','E1DU34.SA','WABC34.SA','CRFB3.SA','USSX34.SA','CSAN3.SA','R1KU34.SA','C1OU34.SA','EGIE3.SA','PRIO3.SA','E2ST34.SA','T2PX34.SA','TIMS3.SA','EQTL3.SA','MACY34.SA','T1AL34.SA','CMIG4.SA','N1WL34.SA','L1MN34.SA','WUNI34.SA','CMIG3.SA','HYPE3.SA','T1EC34.SA','ASAI3.SA','W1IX34.SA','A1IV34.SA','P2EN34.SA','D2KN34.SA','W1BO34.SA','CXSE3.SA','E2EF34.SA','P1VH34.SA','V1NO34.SA','T2DH34.SA','U1AI34.SA','L1EG34.SA','GOLL4.SA','CMIN3.SA','KLBN3.SA','CCRO3.SA','KLBN4.SA','C1AB34.SA','LREN3.SA','W2YF34.SA','CPLE3.SA','ENGI4.SA','I1AC34.SA','CSNA3.SA','CPLE6.SA','MGLU3.SA','BRKM5.SA','ENGI3.SA','CPLE5.SA','A1YX34.SA','ENEV3.SA','BRKM3.SA','NEOE3.SA','ENMT4.SA','ENMT3.SA','VBBR3.SA','TOTS3.SA','RIGG34.SA','TRPL4.SA','TRPL3.SA','CGAS5.SA','CGAS3.SA','NTCO3.SA','ALUP11.SA','STOC31.SA','EQPA3.SA','K1SS34.SA','AURE3.SA','EQPA7.SA','GOAU3.SA','PSSA3.SA','GOAU4.SA','A2MC34.SA','UGPA3.SA','T1RI34.SA','PAGS34.SA','XRXB34.SA','CIEL3.SA','GMAT3.SA','MDIA3.SA','MULT3.SA','VAMO3.SA','REDE3.SA','ENGI11.SA','H1BI34.SA','TAEE3.SA','TAEE4.SA','ENBR3.SA','BRAP3.SA','S1LG34.SA','BRAP4.SA','EMBR3.SA','K2CG34.SA','MRSA5B.SA','A1LL34.SA','INTB3.SA','CEEB3.SA','ALPA4.SA','SLCE3.SA','UNIP6.SA','UNIP3.SA','ALUP4.SA','ALPA3.SA','USIM3.SA','ARZZ3.SA','UNIP5.SA','SULA11.SA','USIM5.SA','SMTO3.SA','RECV3.SA','AMER3.SA','SMFT3.SA','BRFS3.SA','SOMA3.SA','ALUP3.SA','BEEF3.SA','GGPS3.SA','DASA3.SA','U2PW34.SA','WHRL3.SA','WHRL4.SA','BPAN4.SA','BNBR3.SA','EKTR4.SA','EKTR3.SA','BRML3.SA','RRRP3.SA','STBP3.SA','CBAV3.SA','BSLI4.SA','GRND3.SA','DXCO3.SA','CSMG3.SA','F1SL34.SA','F2VR34.SA','AESB3.SA','MOAR3.SA','FLRY3.SA','BSLI3.SA','SIMH3.SA','MEGA3.SA','SAPR4.SA','SAPR3.SA','CYRE3.SA','VIVA3.SA','VVEO3.SA','PCAR3.SA','ODPV3.SA','FESA4.SA','BLAU3.SA','LWSA3.SA','PORT3.SA','MRFG3.SA','SULA3.SA','GETT3.SA','ALSO3.SA','VGIR11.SA','SULA4.SA','GETT4.SA','TTEN3.SA','B2YN34.SA','SAPR11.SA','ABCB4.SA','BRSR6.SA','BRSR3.SA','EQMA3B.SA','INBR32.SA','GPRO34.SA','KNCR11.SA','VIIA3.SA','BRSR5.SA','COGN3.SA','TUPY3.SA','BOAS3.SA','MRVE3.SA','AZUL4.SA','ARML3.SA','LEVE3.SA','CSRN3.SA','CSRN5.SA','GPAR3.SA','CURY3.SA','HGLG11.SA','JHSF3.SA','GUAR3.SA','LOGN3.SA','ONCO3.SA','V2ME34.SA','CBEE3.SA','ENAT3.SA','PETZ3.SA','IGTI3.SA','SBFG3.SA','EZTC3.SA','VULC3.SA','ECOR3.SA','CAML3.SA','YDUQ3.SA','MOVI3.SA','BRPR3.SA','MLAS3.SA','RAPT3.SA','POMO3.SA','AGRO3.SA','RAPT4.SA','FRAS3.SA','POMO4.SA','CEED3.SA','CEED4.SA','XPLG11.SA','PARD3.SA','MILS3.SA','LAND3.SA','AALR3.SA','ORVR3.SA','GEPA3.SA','GEPA4.SA','MATD3.SA','AMBP3.SA','JALL3.SA','AURA33.SA','DIRR3.SA','KNRI11.SA','CLSC4.SA','RECR11.SA','BTLG11.SA','IRBR3.SA','RANI3.SA','BEES4.SA','MYPK3.SA','VITT3.SA','BEES3.SA','LIGT3.SA','VISC11.SA','KEPL3.SA','PGMN3.SA','HBSA3.SA','TASA3.SA','QUAL3.SA','TASA4.SA','JSLG3.SA','LOGG3.SA','HFOF11.SA','TFCO4.SA','BRCR11.SA','ANIM3.SA','CSED3.SA','BAZA3.SA','PNVL3.SA','MODL3.SA','JSRE11.SA','HGRE11.SA','AGXY3.SA','ZAMP3.SA','ELMD3.SA','BBPO11.SA','TGMA3.SA','BMGB4.SA','FIQE3.SA','SQIA3.SA','HSML11.SA','OIBR3.SA','HGCR11.SA','BMOB3.SA','WIZS3.SA','EMAE4.SA','CVCB3.SA','ROMI3.SA','SOJA3.SA','BRIT3.SA','COCE5.SA','OIBR4.SA','OFSA3.SA','HGBS11.SA','POSI3.SA','CASH3.SA','PTBL3.SA','CRPG6.SA','CRPG5.SA','BMEB3.SA','EVEN3.SA','BMEB4.SA','CLSA3.SA','SCAR3.SA','FHER3.SA','IFCM3.SA','DMMO3.SA','SHUL4.SA','TELB4.SA','VRTA11.SA','LAVV3.SA','KRSA3.SA','ABCP11.SA','SHPH11.SA','TELB3.SA','GTLG11.SA','LJQQ3.SA','EUCA3.SA','WLMM4.SA','BRIV3.SA','DESK3.SA','RBRX11.SA','AERI3.SA','BRIV4.SA','CEBR3.SA','MALL11.SA','RBRF11.SA','VLID3.SA','EUCA4.SA','CEBR5.SA','PLPL3.SA','MEAL3.SA','BRGE8.SA','BRGE11.SA','BRGE3.SA','CEBR6.SA','IRDM11.SA','DEXP4.SA','CEAB3.SA','KNSC11.SA','DEXP3.SA','MELK3.SA','PEAB4.SA','ETER3.SA','PEAB3.SA','PEAB3.SA','TRIS3.SA','DOHL4.SA','OPCT3.SA','RPAD3.SA','TRAD3.SA','RPAD6.SA','BCRI11.SA','AFLT3.SA','SDIL11.SA','SEER3.SA','CGRA4.SA','RBRL11.SA','CGRA3.SA','CRIV3.SA','ALLD3.SA','APER3.SA','CRIV4.SA','BCFF11.SA','MTSA4.SA','ESPA3.SA','PQDP11.SA','CSUD3.SA','SEQL3.SA','MDNE3.SA','RNEW4.SA','RNEW3.SA','BIOM3.SA','HBRE3.SA','TEND3.SA','MXRF11.SA','PFRM3.SA','AMAR3.SA','NVHO11.SA','RNEW11.SA','MTRE3.SA','MFII11.SA','HABT11.SA','FCFL11.SA','MFCR11.SA','CARE11.SA','RBVA11.SA','LVTC3.SA','PTNT4.SA','NGRD3.SA','ALPK3.SA','PTNT3.SA','BGIP3.SA','BGIP4.SA','PORD11.SA','CSAB4.SA','FIIB11.SA','BCIA11.SA','MBLY3.SA','HBOR3.SA','RDNI3.SA','G2DI33.SA','BAHI3.SA','LPSB3.SA','CAMB3.SA','BBFI11B.SA','GFSA3.SA','PRNR3.SA','GPIV33.SA','QAGR11.SA','PDTC3.SA','JOPA3.SA','LUXM4.SA','PPLA11.SA','TCSA3.SA','ENJU3.SA','INEP3.SA','DMVF3.SA','INEP4.SA','JASC11.SA','PMAM3.SA','HBTS5.SA','PLCR11.SA','VLOL11.SA','BPFF11.SA','TPIS3.SA','AHEB3.SA','AHEB6.SA','RSUL4.SA','UCAS3.SA','EALT4.SA','FLMA11.SA','DOTZ3.SA','TECN3.SA','EALT3.SA','CXAG11.SA','CXCI11.SA','ONEF11.SA','EPAR3.SA','AVLL3.SA','SHOW3.SA','BBRC11.SA','BOBR4.SA','NINJ3.SA','VCRR11.SA','BLCA11.SA','RNGO11.SA','FIGS11.SA','BMKS3.SA','WEST3.SA','CTNM4.SA','CTNM3.SA','PRSN11B.SA','MGCR11.SA','PLAS3.SA','LLIS3.SA','LUPA3.SA','RPMG3.SA','BMLC11.SA','BALM3.SA','BALM4.SA','AZEV4.SA','AZEV3.SA','FPAB11.SA','MNDL3.SA','SNCI11.SA','CEOC11.SA','HUCG11.SA','CTKA3.SA','CTKA4.SA','FAED11.SA','GCRI11.SA','BMIN4.SA','PINE4.SA','RBED11.SA','EURO11.SA','OURE11.SA','BNFS11.SA','SGPS3.SA','VIVR3.SA','CBOP11.SA','DVFF11.SA','RBRS11.SA','FAMB11B.SA','MGHT11.SA','SPTW11.SA','ITIT11.SA','CXCE11B.SA','RBRD11.SA','RBOP11.SA','JFEN3.SA','CTSA4.SA','CTSA3.SA','ATOM3.SA','CEDO4.SA','ROOF11.SA','RSID3.SA','DTCY3.SA','FATN11.SA','MGEL4.SA','EDFO11B.SA','DRIT11B.SA','BIME11.SA','MNPR3.SA','RCSL4.SA','RCSL3.SA','NEXP3.SA','IGBR3.SA','APTO11.SA','XPCM11.SA','PDGR3.SA','MWET4.SA','BLMC11.SA','FIVN11.SA','TXRX4.SA','CTXT11.SA','CALI3.SA','SLED4.SA','SLED3.SA','SNSY5.SA','ATMP3.SA','SNSY3.SA','FMOF11.SA','PRSV11.SA','NORD3.SA','HAGA4.SA','SCPF11.SA','GCFF11.SA','PLRI11.SA','OSXB3.SA','HAGA3.SA','CXTL11.SA','PABY11.SA','RNDP11.SA','BDLL3.SA','BDLL4.SA','HOOT4.SA','TEKA4.SA','RBVO11.SA','FRTA3.SA','HETA4.SA','RBDS11.SA','PNPR11.SA','GRMZ5L.SA','FSTU11.SA','EQPA7F.SA','HBCR11.SA','COCE3F.SA','SRVD11.SA','PEVC11.SA','ENMT3F.SA','ESTR4F.SA','JOPA3F.SA','C2CA34.SA','E2LS34.SA','F2RT34.SA','N2VC34.SA','L2AZ34.SA','RBHY12.SA','BCWV39.SA','BVLU39.SA','BEFV39.SA','FZDA11.SA','TF495.SA','ZIFI11.SA','TF545.SA','TF525.SA','TF693.SA','TF573.SA','TF703.SA','TF473.SA','TF685.SA','BDLL4F.SA','BPAR3F.SA','BAAX39.SA','G1DS34.SA','BREV11.SA','FPOR11.SA','BUTL39.SA','SNSY5F.SA','BEWW39.SA','BAHI3F.SA','CJCT11.SA','LASC11.SA','RBIR11.SA','CBEE3F.SA','U2PS34.SA','BSOX39.SA','BIOM3F.SA','HGIC11.SA','REIT11.SA','PEAB3F.SA','RSUL4F.SA','RPAD3F.SA','BSIL39.SA','BIJH39.SA','EQMA3BF.SA','BIYE39.SA','EMAE4F.SA','MNPR3F.SA','BIVE39.SA','AGXY3F.SA','BIDB11.SA','LUXM4F.SA','IFCM3F.SA','IGBR3F.SA','BMIL39.SA','GOVE11.SA','ESGD11.SA','CRIV3F.SA','JRDM11.SA','BIVW39.SA','NORD3F.SA','TFCO4F.SA','W1BD34.SA','FLCR11.SA','BEDC39.SA','BHYG39.SA','BGRT39.SA','H2TA34.SA','BOTZ39.SA','BLPX39.SA','MERC4F.SA','EKTR3F.SA','USAL11.SA','HAGA4F.SA','OFSA3F.SA','HCRI11.SA','BURA39.SA','EQPA3F.SA','IRFM11.SA','NEWU11.SA','PNVL3F.SA','LLIS3F.SA','CGRA4F.SA','SLED4F.SA','USDB11.SA','BACW39.SA','AGRI11.SA','PDTC3F.SA','POSI3F.SA','BITH11.SA','CLSA3F.SA','CRPT11.SA','TIMS3F.SA','BAZA3F.SA','NEWU11.SA','BMEB4F.SA','ENGI3F.SA','BITI11.SA','BTLT39.SA','SEQL3F.SA','ETER3F.SA','MLAS3F.SA','HCRI11.SA','SHOT11.SA','MDIA3F.SA','CEBR6F.SA','IRFM11.SA','QDFI11.SA','QAMI11.SA','ATMP3F.SA','PORT3F.SA','OFSA3F.SA','BURA39.SA','GFSA1.SA','BITH11.SA','ALUP3F.SA','CLSA3F.SA','ESGD11.SA','GFSA1F.SA','PNVL3F.SA','HTMX11.SA','TFCO4F.SA','LLIS3F.SA','LEVE3F.SA','SOJA3F.SA','RBRY11.SA','NASD11.SA','SAPR4F.SA','GRND3F.SA','CASH3F.SA','ELET3F.SA','CURY3F.SA','COGN3F.SA','AGRX11.SA','GGPS3F.SA','MEAL3F.SA','BRIV3F.SA','BBAS3F.SA','FGAA11.SA','POSI3F.SA','ARCT11.SA','VIIA3F.SA','HCTR11.SA','TAEE11F.SA','VIVT3F.SA','BAAX39.SA','ENEV3F.SA','FLRY3F.SA','PDGR3F.SA','SUZB3F.SA','YDRO11.SA','PSSA3F.SA','BMOB3F.SA','XFIX11.SA','ALUP11F.SA','VOTS11.SA','MULT3F.SA','BOVV11.SA','JHSF3F.SA','BRML3F.SA','CSNA3F.SA','TIMS3F.SA','USDB11.SA','REDE3F.SA','KNIP11.SA','ENBR3F.SA','KNHY11.SA','VIVA3F.SA','XPML11.SA','VIFI11.SA','XINA11.SA','OUJP11.SA','KIVO11.SA','JSLG3F.SA','MNPR3F.SA','VITT3F.SA','CPLE6F.SA','VLID3F.SA','SPXI11.SA','CSUD3F.SA','RANI3F.SA','POMO4F.SA','PETR3F.SA','SAPR3F.SA','PFIN11.SA','SHOW3F.SA','SARE11.SA','ARRI11.SA','VVEO3F.SA','LAVV3F.SA','PTBL3F.SA','BOVA11.SA','GGRC11.SA','VIFI11.SA','XINA11.SA','KIVO11.SA','ARCT11.SA','FGAA11.SA','BBAS3F.SA','RCFF11.SA','ENMT4F.SA','FRIO3F.SA','TXRX3F.SA','EQPA5F.SA','BLUR11.SA','CRPG3F.SA','CASN3F.SA','HDEL11.SA','SLED3F.SA','FLRP11.SA','C2OL34.SA','S2FM34.SA','A2SO34.SA','M2RT34.SA','BIYC39.SA','ZAVI11.SA','WSEC11.SA','MOAR3F.SA','BAER39.SA','BIEU39.SA','HOOT4F.SA','CXRI11.SA','Q2SC34.SA','BEWJ39.SA','BEWY39.SA','BIWF39.SA','BEWT39.SA','BEWQ39.SA','BSDV39.SA','EXES11.SA','IMBB11.SA','EQPA6F.SA','MCHY11.SA','N2TN34.SA','M2PR34.SA','ODER4F.SA','O2NS34.SA','RMAI11.SA','A2RE34.SA','HOSI11.SA','C2RW34.SA','XPHT11.SA','TF665.SA','TF713.SA','TF485.SA','TF535.SA','TF515.SA','TF519.SA','V2MW34.SA','TF505.SA','TF585.SA','BKSA39.SA','M2RV34.SA','SCVB11.SA','CSRN6F.SA','BSLV39.SA','WEB311.SA','BMEB3F.SA','ENDD11.SA','KNOX11.SA','BICR11.SA','BEEM39.SA','BDRI39.SA','RNEW2.SA','RBIF11.SA','FIXA11.SA','RNEW1F.SA','RNEW11F.SA','RCFA11.SA','FESA3F.SA','OGIN11.SA','HAGA3F.SA','BRSR5F.SA','TRIG11.SA','CEDO3F.SA','BALM4F.SA','CBAV3F.SA','EQTL3F.SA','URET11.SA','DMVF3F.SA','LREN3F.SA','MGFF11.SA','ROMI3F.SA','TRPL4F.SA','SANB11F.SA','IFRA11.SA','BLAU3F.SA','FNAM11.SA','RNEW1.SA','EZTC3F.SA','BLMR11.SA','TASA3F.SA','MILS3F.SA','BMTU39.SA','PFRM3F.SA','BTAG11.SA','RCSL4F.SA','JFLL11.SA','DESK3F.SA','ONCO3F.SA','ECOR3F.SA','IDFI11.SA','GPAR3F.SA','E2NP34.SA','AZEV4F.SA','CRPG6F.SA','BIEM39.SA','ATSA11.SA','RSID3F.SA','GENB11.SA','PATC11.SA','RNEW2F.SA','BRBI11F.SA','RDPD11.SA','TASA3F.SA','MILS3F.SA','WHRL4F.SA','OSXB3F.SA','USTK11.SA','INTB3F.SA','MYPK3F.SA','CMIG3F.SA','ITUB3F.SA','MWET4F.SA','MILL11.SA','ALSO3F.SA','HSLG11.SA','SVAL11.SA','EMBR3F.SA','ANIM3F.SA','BIEF39.SA','RADL3F.SA','QBTC11.SA','URET11.SA','DMVF3F.SA','SANB11F.SA','IFRA11.SA','CBAV3F.SA','PATL11.SA','BOVB11.SA','WRLD11.SA','BDIF11.SA','MODL3F.SA','GFSA3F.SA','ATOM3F.SA','JPPA11.SA','AESB1F.SA','GOLD11.SA','OPCT3F.SA','LREN3F.SA','ROMI3F.SA','TRPL4F.SA','MGFF11.SA','TGAR11.SA','LVBI11.SA','TTEN3F.SA','MCHF11.SA','RAIZ4.SA','ARML3F.SA','BOVX11.SA','EZTC3F.SA','EQTL3F.SA','BLMR11.SA','NEOE3F.SA','BLAU3F.SA','CIEL3F.SA','BPAC11F.SA','DIVO11.SA','SNAG11.SA','SANB3F.SA','GTWR11.SA','LPSB3F.SA','KFOF11.SA','BTCI11.SA','CPLE3F.SA','CMIN3F.SA','BRKM5F.SA','VULC3F.SA','CXSE3F.SA','ENGI11F.SA','FNAM11.SA','VSLH11.SA','RBRP11.SA','ITSA3F.SA','MOVI3F.SA','VAMO3F.SA','RCRB11.SA','VIVR3F.SA','AERI3F.SA','CPLE11.SA','BBDC3F.SA','HGFF11.SA','FESA4F.SA','QBTC11.SA','BTCI11.SA','CPLE3F.SA','BRKM5F.SA','PGMN3F.SA','ODPV3F.SA','CYCR11.SA','PVBI11.SA','VXXV11.SA','ABGD39.SA','NUTR3F.SA','ERPA11.SA','MNHT5L.SA','PATI3F.SA','TKNO4F.SA','ESTR3F.SA','TSER11.SA','BKYY39.SA','HCRA11.SA','AHEB3F.SA','ESUT11F.SA','CSRN5F.SA','CSAB4F.SA','AVLL3F.SA','DTCY3F.SA','CEED4F.SA','S2WA34.SA','Z2SC34.SA','BIXG39.SA','BXTC39.SA','BSUS39.SA','WTSP11B.SA','ELET5F.SA','FSRF11.SA','BURT39.SA','BSHY39.SA','BIYF39.SA','BBCN39.SA','B5MB11.SA','BKCH39.SA','TF513.SA','TF681.SA','TF503.SA','TF675.SA','T2ER34.SA','TF563.SA','TF543.SA','BKXI39.SA','A2MB34.SA','E1DI34.SA','BXPO11.SA','S2NA34.SA','PTNT3F.SA','ESGU11.SA','L2PL34.SA','EPAR3F.SA','BIXJ39.SA','HSRE11.SA','PEMA11.SA','S2TA34.SA','WLMM3F.SA','SMAB11.SA','XPHT12.SA','BBOV11.SA','FSPE11F.SA','META11.SA','DEBB11.SA','S2TW34.SA','XBOV11.SA','RECX11.SA','HTEK11.SA','HUSC11.SA','P2AN34.SA','USIM6F.SA','NFTS11.SA','ISUS11.SA','NINJ3F.SA','BDVD39.SA','BEWL39.SA','CALI3F.SA','CEEB3F.SA','CPTI11.SA','BHEF39.SA','CORN11.SA','DEXP3F.SA','BOBR4F.SA','BDIV11.SA','ESGB11.SA','BBUG39.SA','FSRF11F.SA','LOGN3F.SA','MFAI11.SA','RFOF11.SA','ACWI11.SA','GMAT3F.SA','L2RN34.SA','MAPT4F.SA','CLSC3F.SA','UGPA3F.SA','BEWG39.SA','USIM3F.SA','MTRE3F.SA','TUPY3F.SA','WEST3F.SA','BRKM6F.SA','INEP4F.SA','DEXP3F.SA','5GTK11.SA','BEWL39.SA','CALI3F.SA','BOBR4F.SA','TRAD3F.SA','JFEN3F.SA','XMAL11.SA','UNIP5F.SA','SCAR3F.SA','GETT4F.SA','RFOF11.SA','CPTI11.SA','FSRF11F.SA','L2RN34.SA','MAPT4F.SA','CEEB3F.SA','CLSC3F.SA','IRIM11.SA','NFTS11.SA','ISUS11.SA','ESGB11.SA','LOGN3F.SA','BIJR39.SA','BBGO11.SA','UGPA3F.SA','FVPQ11.SA','VSHO11.SA','OIAG11.SA','CRFB3F.SA','MATB11.SA','SULA4F.SA','IGTI11F.SA','ENJU3F.SA','CEBR3F.SA','DAMT11B.SA','CTSA4F.SA','BOAS3F.SA','GGBR3F.SA','TPIS3F.SA','VCRI11.SA','BLQD39.SA','RNEW12F.SA','STBP3F.SA','RECX11.SA','YDUQ3F.SA','SMFT3F.SA','ITUB4F.SA','XPPR11.SA','TAEE3F.SA','VGHF11.SA','MORC11.SA','CACR11.SA','VCJR11.SA','CMIG4F.SA','ESPA3F.SA','ITSA4F.SA','PICE11.SA','NTCO3F.SA','NINJ3F.SA','XPSF11.SA','CORN11.SA','ACWI11.SA','OULG11.SA','ALPA4F.SA','TEPP11.SA','BEWG39.SA','MRFG3F.SA','TOTS3F.SA','BDVD39.SA','IRBR3F.SA','BEES4F.SA','UNIP3F.SA','CPTR11.SA','SPXB11.SA','BDIV11.SA','ALUP4F.SA','VGIP11.SA','AURE3F.SA','AFHI11.SA','JSAF11.SA','GOLL4F.SA','XPCA11.SA','XPID11.SA','KISU11.SA','LOGG3F.SA','BARI11.SA','BBSE3F.SA','ABEV3F.SA','UNIP6F.SA','GGBR4F.SA','AZUL4F.SA','VTLT11.SA','HASH11.SA','IGTI11F.SA','CLSC4F.SA','BRKM6F.SA','TAEE3F.SA','XPPR11.SA','MORC11.SA','VGHF11.SA','CACR11.SA','SULA4F.SA','XPSF11.SA','BGIP3F.SA','CEEB5F.SA','BRGE11F.SA','DMFN3F.SA','LIPR3F.SA','CCME11.SA','BQCL39.SA','CEDO4F.SA','F2IC34.SA','F2IV34.SA','GEPA3F.SA','TEKA3F.SA','F2RS34.SA','BEWP39.SA','HAAA11.SA','AHEB5F.SA','VSEC11.SA','BZRO39.SA','BRLA11.SA','CTKA4F.SA','BFXI39.SA','BICL39.SA','I2RS34.SA','J2AZ34.SA','WLMM4F.SA','BRIV4F.SA','BDOM11.SA','BQUA39.SA','TF523.SA','TF493.SA','TF655.SA','TF623.SA','A2XO34.SA','BEWU39.SA','TF553.SA','TF593.SA','FPNG11.SA','BIBB39.SA','IBOB11.SA','BDVY39.SA','TRNT11.SA','NAVT11.SA','SIVR39.SA','PSVM11F.SA','BICE11.SA','S2CH34.SA','BGIP4F.SA','TXRX4F.SA','BGNO39.SA','BPFV39.SA','BLPA39.SA','BPVE39.SA','BFNX39.SA','EUCA3F.SA','RBLG11.SA','BSCZ39.SA','PLCA11.SA','CTNM4F.SA','PEAB4F.SA','BCLO39.SA','BCHQ39.SA','EKTR4F.SA','FSTU11F.SA','NEXP3F.SA','RCSL3F.SA','GDXB39.SA','HGAG11.SA','DESK1F.SA','GURU11.SA','CPLE5F.SA','GETT3F.SA','KCRE11.SA','TGMA3F.SA','CTNM3F.SA','CPFF11.SA','O2HI34.SA','LUGG11.SA','ITIP11.SA','HBSA3F.SA','ALMI11.SA','PINE4F.SA','BSLI4F.SA','BRAX11.SA','BSLI3F.SA','CSRN3F.SA','BIEV39.SA','HPDP11.SA','ALLD3F.SA','BEWZ39.SA','BBOI11.SA','TECN3F.SA','DASA3F.SA','GEPA4F.SA','LJQQ3F.SA','ITIP11.SA','HGAG11.SA','XPIE11.SA','BIEI39.SA','CSED3F.SA','RCSL3F.SA','EUCA4F.SA','ESGE11.SA','FIQE3F.SA','FNOR11.SA','TEND3F.SA','BEWC39.SA','BUSR39.SA','CCRF11.SA','AFLT3F.SA','BIXN39.SA','BRSR3F.SA','HSAF11.SA','HGPO11.SA','FHER3F.SA','HBSA3F.SA','GDXB39.SA','L2SI34.SA','GUAR3F.SA','CPLE5F.SA','O2HI34.SA','LUGG11.SA','ENGI4F.SA','BEES3F.SA','MEGA3F.SA','KINP11.SA','LAND3F.SA','ALLD3F.SA','DESK1F.SA','LIGT3F.SA','INEP3F.SA','NCHB11.SA','LGCP11.SA','NEWL11.SA','ARZZ3F.SA','PCAR3F.SA','PLPL3F.SA','NGRD3F.SA','CPFF11.SA','KCRE11.SA','AESB1.SA','BRBI11.SA','SEER3F.SA','SAPR11F.SA','RURA11.SA','CSMG3F.SA','GETT3F.SA','CYRE3F.SA','GOAU4F.SA','TAEE4F.SA','AGRO3F.SA','ETHE11.SA','SHUL4F.SA','REVE11.SA','PETZ3F.SA','IGTI11.SA','DEVA11.SA','BRCO11.SA','SMAL11.SA','BRAP4F.SA','KEPL3F.SA','XPIN11.SA','GALG11.SA','JURO11.SA','MCCI11.SA','RZAG11.SA','AIEC11.SA','SOMA3F.SA','SMTO3F.SA','CXCO11.SA','CSAN3F.SA','TORD11.SA','VILG11.SA','EGIE3F.SA','BTRA11.SA','RAIZ4F.SA','RZAK11.SA','IVVB11.SA','CCRO3F.SA','RECV3F.SA','SQIA3F.SA','SMAC11.SA','TRXF11.SA','SIMH3F.SA','EVEN3F.SA','ELET6F.SA','CVCB3F.SA','BBFO11.SA','HAPV3F.SA','B3SA3F.SA','MRVE3F.SA'



textoArray2 = 'TORD11.SA','VILG11.SA','EGIE3F.SA','BTRA11.SA','RAIZ4F.SA','RZAK11.SA','IVVB11.SA','CCRO3F.SA','RECV3F.SA','SQIA3F.SA','SMAC11.SA','TRXF11.SA'