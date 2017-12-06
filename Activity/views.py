from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_control
from login.models import Login
import xlsxwriter
import openpyxl
from .models import StandaloneTestBedSetup, UcsmTestBedSetup, TestExecution, StandaloneTestBedSetupFinal, UcsmTestBedSetupFinal
from django.http import HttpResponse
from pprint import pprint as pp
import re
import xlwt
from xlrd import open_workbook
from flask import json
from django.contrib.auth.decorators import login_required
import time
from login.models import Login
from django.db.models import Q


def adapter_alias():
    adapter_names = []

    file_location = "C:/Users/pyogaraj/Desktop/Alias_sheet.xlsx"
    book = open_workbook(file_location)
    sheet = book.sheet_by_index(0)
    adapter_names.append('Adapter')
    for rows in range(1, sheet.nrows):
        # adapter_names[sheet.cell_value(rows, 0).strip()] = sheet.cell_value(rows, 1).rstrip()
        adapter_names.append(sheet.cell_value(rows, 1).rstrip())

        # pp(adapter_nickname)
        # exit(0)
    return adapter_names


def os_names():
    os_name = []

    file_location = "C:/Users/pyogaraj/Desktop/OS_Platforms_PRD.xls"
    book = open_workbook(file_location)
    sheet = book.sheet_by_index(0)

    for rows in range(1, sheet.nrows):
        os_name.append(sheet.cell_value(rows, 0).strip())
    os_name.insert(0, 'OS')

    return os_name


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def dashboard(request):

    leads = ['shpr', 'giraj', 'mmylsamy', 'mugrukri', 'sarramas', 'pyogaraj']
    if request.method == 'POST':
        shit = ['shpr','pyogaraj']
        nname = ''

        uname = request.POST.get('uname')
        pswd = request.POST.get('pswd')
        #if uname not in shit:
            #return HttpResponse("<h1>Website is loading......Please be patient</h1>")
        if uname == 'abkaliy':
            return render(request, 'figure.html')
        request.session['uname'] = uname
        user_existence = Login.objects.filter(user__startswith=str(uname))
        for nn in user_existence:
            nname = nn.nickname

        standalone_testbed = StandaloneTestBedSetup.objects.filter(engineer__startswith=str(nname))
        ucsm_testbed = UcsmTestBedSetup.objects.filter(engineer__startswith=str(nname))
        # print str(uname)
        # print user_existence
        adapter_names = adapter_alias()
        os_name = os_names()
        if uname not in leads:
            lead = 0
        else:
            lead = 1

        context = {
            'user_existence': user_existence,
            'standalone_testbed': standalone_testbed,
            'ucsm_testbed': ucsm_testbed,
            'adapter_names': json.dumps(adapter_names),
            'os_name': json.dumps(os_name),
            'lead': lead,
        }
        if not user_existence:
            return render(request, 'nouser.html')
        else:
            for username in user_existence:
                if pswd == username.pswd:
                    # return HttpResponse(data)
                    print 'standalone content is'
                    # for dumb in standalone_testbed:
                    #     print dumb.cimc_ip
                    #     exit(0)
                    return render(request, 'newhtml1.html', context)
                else:
                    return render(request, 'login_pswd.html')
    elif request.method == 'GET':

        return render(request, 'error404.html')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def testbed(request):
    uname_t = request.session['uname']
    user_existence = Login.objects.filter(user__startswith=str(uname_t))
    adapter_names = adapter_alias()
    os_name = os_names()

    context = {
        'user_existence': user_existence,
        'adapter_names': json.dumps(adapter_names),
        'os_name': json.dumps(os_name),
    }
    return render(request, 'TestBedSetup.html', context)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def preview(request):
    input_activity_data = {}
    teams_inserted = []
    position = 1

    for i in range(0, 20):
        # try:
            if request.method == 'POST':
                teams = request.POST.getlist('actlabel')
                print "teams in preview"
                pp(teams)
                if request.POST.getlist('actlabel'):
                    for team in teams:
                        if re.match('.*', team):
                            teams_inserted.append(team)
                            drive = ''
                            adapt = ''
                            drivers = request.POST.getlist('driver')
                            adapters = request.POST.getlist('adapter')
                            for d in drivers:
                                if drive == '':
                                    drive = d
                                else:
                                    drive = drive + ',' + d
                            for a in adapters:
                                if adapt == '':
                                    adapt = a
                                else:
                                    adapt = adapt + ',' + a
                            if team not in teams_inserted:
								try:
									input_activity_data[team] = {'testbed':team, 'automationused':request.POST.get('auto_type' + str(position)), 'os_type':request.POST.get('os_name' + str(position)),
																 'cdetsID':request.POST.get('LinkForLogs' + str(position)), 'os_bmode':request.POST.get('Boot_Type' + str(position)), 'logs':request.POST.get('Link_Automation' + str(position)),
																 'comments':request.POST.get('Remarks' + str(position)), 'res':request.POST.get('Result' + str(position)),
																 'driver_version':request.POST.getlist('driver' + str(position)), 'pxe_adapter':request.POST.get('Pxe_adapter' + str(position)), 'adapters':request.POST.getlist('adapter' + str(position)),
																 'bootType':request.POST.get('server_boottype' + str(position)), 'effort':request.POST.get('Effortspent' + str(position))}
								except IndexError:
									print 'inside IndexError'
									input_activity_data[team] = {'testbed':team, 'automationused':request.POST.get('auto_type' + str(position)), 'os_type':request.POST.get('os_name' + str(position)),
																 'cdetsID':request.POST.get('LinkForLogs' + str(position)), 'os_bmode':request.POST.get('Boot_Type' + str(position)), 'logs':'NA',
																 'comments':request.POST.get('Remarks' + str(position)), 'res':request.POST.get('Result' + str(position)),
																 'driver_version':request.POST.getlist('driver' + str(position)), 'pxe_adapter':'NA', 'adapters':request.POST.getlist('adapter' + str(position)),
																 'bootType':request.POST.get('server_boottype' + str(position)), 'effort':request.POST.get('Effortspent' + str(position))}
								position += 1
                            else:
								try:
									input_activity_data[team + "(" + str(position) + ")"] = {'testbed':team, 'automationused':request.POST.get('auto_type' + str(position)), 'os_type':request.POST.get('os_name' + str(position)),
																 'cdetsID':request.POST.get('LinkForLogs' + str(position)), 'os_bmode':request.POST.get('Boot_Type' + str(position)), 'logs':request.POST.get('Link_Automation' + str(position)),
																 'comments':request.POST.get('Remarks' + str(position)), 'res':request.POST.get('Result' + str(position)),
																 'driver_version':request.POST.getlist('driver' + str(position)), 'pxe_adapter':request.POST.get('Pxe_adapter' + str(position)), 'adapters':request.POST.getlist('adapter' + str(position)),
																 'bootType':request.POST.get('server_boottype' + str(position)), 'effort':request.POST.get('Effortspent' + str(position))}
								except IndexError:
									print 'inside IndexError'
									input_activity_data[team + "(" + str(position) + ")"] = {'testbed':team, 'automationused':request.POST.get('auto_type' + str(position)), 'os_type':request.POST.get('os_name' + str(position)),
																 'cdetsID':request.POST.get('LinkForLogs' + str(position)), 'os_bmode':request.POST.get('Boot_Type' + str(position)), 'logs':'NA',
																 'comments':request.POST.get('Remarks' + str(position)), 'res':request.POST.get('Result' + str(position)),
																 'driver_version':request.POST.getlist('driver' + str(position)), 'pxe_adapter':'NA', 'adapters':request.POST.getlist('adapter' + str(position)),
																 'bootType':request.POST.get('server_boottype' + str(position)), 'effort':request.POST.get('Effortspent' + str(position))}
								position += 1

                pp(input_activity_data)
                uname_prev = request.session['uname']
                user_existence = Login.objects.filter(user__startswith=str(uname_prev))
                nname = ''
                for nn in user_existence:
                    nname = nn.nickname

                standalone_testbed = StandaloneTestBedSetupFinal.objects.filter(engineer__startswith=str(nname))
                ucsm_testbed = UcsmTestBedSetupFinal.objects.filter(engineer__startswith=str(nname))
                context1 = {
                    'input_activity_data': input_activity_data,
                    'standalone_testbed': standalone_testbed,
                    'ucsm_testbed': ucsm_testbed,
                }
                # return HttpResponse(template.render(context, request))
                return render(request, 'preview.html', context1)
            else:
                return render(request, 'error404.html')
        # except TypeError or AttributeError:
        #     pp(input_activity_data)
        #     exit(0)


def delete(request):
    delete_tb = request.POST.getlist("checks")
    uname_del = request.session['uname']
    user_existence = Login.objects.filter(user__startswith=str(uname_del))
    nname = ''
    for nn in user_existence:
        nname = nn.nickname

    standalone_testbed = StandaloneTestBedSetup.objects.filter(engineer__startswith=str(nname))
    ucsm_testbed = UcsmTestBedSetup.objects.filter(engineer__startswith=str(nname))
    os_name = os_names()
    context = {
        'user_existence': user_existence,
        'standalone_testbed': standalone_testbed,
        'ucsm_testbed': ucsm_testbed,
        'os_name':json.dumps(os_name),
    }
    for data in delete_tb:
        for tb in standalone_testbed:
            if data == tb.cimc_ip:
                tb.delete()
        for tb in ucsm_testbed:
            if data == tb.fi_ip + '_' + tb.server_type:
                tb.delete()

    return render(request, 'newhtml1.html', context)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def tb_modify(request):
    uname_tb = request.session['uname']
    user_existence = Login.objects.filter(user__startswith=str(uname_tb))
    nname = ''
    for nn in user_existence:
        nname = nn.nickname

    standalone_testbed = StandaloneTestBedSetup.objects.filter(engineer__startswith=str(nname))
    ucsm_testbed = UcsmTestBedSetup.objects.filter(engineer__startswith=str(nname))
    context1 = {
        'standalone_testbed': standalone_testbed,
        'ucsm_testbed': ucsm_testbed,
    }
    return render(request, 'tb_modify.html', context1)


def save(request):
    testbed_data = {}
    inserted = []
    stand_position = 0
    ucsm_position = 0
    adap_pos = 0;
    nname = ''

    uname_save = request.session['uname']
    user_existence = Login.objects.filter(user__startswith=str(uname_save))
    for nn in user_existence:
        nname = nn.nickname

    standalone_testbed = StandaloneTestBedSetup.objects.filter(engineer__startswith=str(nname))
    ucsm_testbed = UcsmTestBedSetup.objects.filter(engineer__startswith=str(nname))
    os_name = os_names()
    context1 = {
        'user_existence': user_existence,
        'standalone_testbed': standalone_testbed,
        'ucsm_testbed': ucsm_testbed,
        'os_name': json.dumps(os_name),
    }
    adap_type = []
    slot = []
    adap_fw = []
    target = []
    bootcode = []
    ucsm_adap_type = []
    ucsm_slot = []
    ucsm_adap_fw = []
    ucsm_target = []
    ucsm_bootcode = []

    teams = request.POST.getlist('actlabel')
    cimc = request.POST.getlist('CIMC')
    pswd = request.POST.getlist('cimc_password')
    server_type = request.POST.getlist('Server_name')
    cimc_bios = request.POST.getlist('CIMC_BIOS')
    fw_upg = request.POST.getlist('FW_Upgrade')
    for team in teams:
        if re.match('Rack OS-Compat-Standalone-\d', team):
            adap_type.append(request.POST.getlist('Adapter' + str(adap_pos)))
            slot.append(request.POST.getlist('slot' + str(adap_pos)))
            adap_fw.append(request.POST.getlist('Firmware' + str(adap_pos)))			
            target.append(request.POST.getlist('boot' + str(adap_pos)))
            bootcode.append(request.POST.getlist('Bootcode' + str(adap_pos)))
            adap_pos += 1
        elif re.match('Rack OS-Compat-UCSM-\d', team):
            ucsm_adap_type.append(request.POST.getlist('ucsm_adapter' + str(adap_pos)))
            ucsm_slot.append(request.POST.getlist('ucsmslot' + str(adap_pos)))
            ucsm_adap_fw.append(request.POST.getlist('ucsfirmware' + str(adap_pos)))			
            ucsm_target.append(request.POST.getlist('ucsboot' + str(adap_pos)))
            ucsm_bootcode.append(request.POST.getlist('ucsbios' + str(adap_pos)))
            adap_pos += 1
    effort = request.POST.getlist('standalone_effort')

    fiIp = request.POST.getlist('FI Ip')
    fiFW = request.POST.getlist('FI Firmware')
    serverNum = request.POST.getlist('server_num')
    ucsm_cimcVer = request.POST.getlist('CIMC_Version')
    ucsm_biosVer = request.POST.getlist('BIOS_Version')
    discovery_met = request.POST.getlist('Discovery_method')
    ucsm_server_type = request.POST.getlist('Ucsm_servername')
    u_effort = request.POST.getlist('ucsmeffort')

    if request.POST.getlist('actlabel'):
        for team in teams:
            if team not in inserted:
                inserted.append(team)
                if re.match('Rack OS-Compat-Standalone-\d', team):
                    testbed_data[team] = {'engineer':str(request.POST.get('engineer')), 'cimc':cimc[stand_position], 'server_type':server_type[stand_position],
                                          'cimc_bios':cimc_bios[stand_position], 'fw_upg':fw_upg[stand_position], 'adap_type':adap_type[stand_position],
                                          'slot':slot[stand_position], 'adap_fw':adap_fw[stand_position], 'target_type':target[stand_position], 'bootcode':bootcode[stand_position],
                                          'pswd': pswd[stand_position], 'effort':effort[stand_position]}
                    stand_position += 1
                elif re.match('Rack OS-Compat-UCSM-\d', team):
                    testbed_data[team] = {'engineer':str(request.POST.get('engineer')), 'fiIp': fiIp[ucsm_position], 'fiFW':fiFW[ucsm_position],
                                          'serverNum':serverNum[ucsm_position], 'ucsm_cimcVer':ucsm_cimcVer[ucsm_position], 'ucsm_biosVer':ucsm_biosVer[ucsm_position],
                                          'discovery_met': discovery_met[ucsm_position], 'ucsm_server_type':ucsm_server_type[ucsm_position],
                                          'ucsm_slot': ucsm_slot[ucsm_position], 'ucsm_adap_fw': ucsm_adap_fw[ucsm_position], 'ucsm_adap_type':ucsm_adap_type[ucsm_position],
                                          'ucsm_target': ucsm_target[ucsm_position], 'ucsm_bootcode': ucsm_bootcode[ucsm_position], 'effort':u_effort[ucsm_position]}
                    ucsm_position += 1

    pp(testbed_data)


    for team, data in testbed_data.iteritems():
        standalone = StandaloneTestBedSetup()
        standalone_f = StandaloneTestBedSetupFinal()
        ucsm = UcsmTestBedSetup()
        ucsm_f = UcsmTestBedSetupFinal()
        if re.match('Rack OS-Compat-Standalone-\d', team):
            print data['cimc']
            standalone.engineer = data['engineer']
            standalone.cimc_ip = data['cimc']
            standalone.password = data['pswd']
            standalone.server_type = data['server_type']
            standalone.cimc_bios_version = data['cimc_bios']
            standalone.firmware_upgrade_prs = data['fw_upg']
            standalone.adapter_name = data['adap_type']
            standalone.adapter_slot = data['slot']
            standalone.adapter_fw = data['adap_fw']
            standalone.target_type = data['target_type']
            standalone.bios_bootcode = data['bootcode']
            standalone.effort = data['effort']
            standalone.save()

            standalone_f.engineer = data['engineer']
            standalone_f.cimc_ip = data['cimc']
            standalone_f.password = data['pswd']
            standalone_f.server_type = data['server_type']
            standalone_f.cimc_bios_version = data['cimc_bios']
            standalone_f.firmware_upgrade_prs = data['fw_upg']
            standalone_f.adapter_name = data['adap_type']
            standalone_f.adapter_slot = data['slot']
            standalone_f.adapter_fw = data['adap_fw']
            standalone_f.target_type = data['target_type']
            standalone_f.bios_bootcode = data['bootcode']
            standalone_f.effort = data['effort']
            standalone_f.save()
            #exit(0)
        elif re.match('Rack OS-Compat-UCSM-\d', team):
            ucsm_f.engineer = data['engineer']
            ucsm_f.fi_ip = data['fiIp']
            ucsm_f.fi_firmware = data['fiFW']
            ucsm_f.server_number = data['serverNum']
            ucsm_f.server_type = data['ucsm_server_type']
            ucsm_f.cimc_version = data['ucsm_cimcVer']
            ucsm_f.cimc_bios_version = data['ucsm_biosVer']
            ucsm_f.discovery_methods = data['discovery_met']
            ucsm_f.adapter_name = data['ucsm_adap_type']
            ucsm_f.adapter_slot = data['ucsm_slot']
            ucsm_f.adapter_fw = data['ucsm_adap_fw']
            ucsm_f.target_type = data['ucsm_target']
            ucsm_f.bios_bootcode = data['ucsm_bootcode']
            ucsm_f.effort = data['effort']
            ucsm_f.save()

            ucsm.engineer = data['engineer']
            ucsm.fi_ip = data['fiIp']
            ucsm.fi_firmware = data['fiFW']
            ucsm.server_number = data['serverNum']
            ucsm.server_type = data['ucsm_server_type']
            ucsm.cimc_version = data['ucsm_cimcVer']
            ucsm.cimc_bios_version = data['ucsm_biosVer']
            ucsm.discovery_methods = data['discovery_met']
            ucsm.adapter_name = data['ucsm_adap_type']
            ucsm.adapter_slot = data['ucsm_slot']
            ucsm.adapter_fw = data['ucsm_adap_fw']
            ucsm.target_type = data['ucsm_target']
            ucsm.bios_bootcode = data['ucsm_bootcode']
            ucsm.effort = data['effort']
            ucsm.save()

    return render(request, 'newhtml1.html', context1)


def execution(request):
    final_data = {}
    position = 0
    stand = 0
    ucsm = 0
    pos = 0
    pk_inserted = []
    inserted = []

    setups = request.POST.getlist('setup')
    print "setup's in execution"
    pp(setups)
    uname_execution = request.session['uname']
    user_existence = Login.objects.filter(user__startswith=str(uname_execution))
    nname = ''
    for nn in user_existence:
        nname = nn.nickname

    standalone_testbed_f = StandaloneTestBedSetupFinal.objects.filter(engineer__startswith=str(nname))
    standalone_testbed = StandaloneTestBedSetup.objects.filter(engineer__startswith=str(nname))
    ucsm_testbed_f = UcsmTestBedSetupFinal.objects.filter(engineer__startswith=str(nname))
    ucsm_testbed = UcsmTestBedSetup.objects.filter(engineer__startswith=str(nname))
    os_name = os_names()
    context1 = {
        'user_existence': user_existence,
        'standalone_testbed': standalone_testbed,
        'ucsm_testbed': ucsm_testbed,
        'os_name': json.dumps(os_name),
    }
    for setup in setups:
        if setup not in inserted:
            inserted.append(setup)
            for tb in standalone_testbed_f:
                if re.match('(.*)\-(.*)',setup):
                #if setup == tb.cimc_ip:
                    stand += 1
                    final_data[setup] = {'pk':standalone_testbed_f.filter(id=tb.id), 'engineer':str(nname), 'os':request.POST.getlist('os'), 'os_bootM':request.POST.getlist('os_bootm'), 'os_bootT':request.POST.getlist('os_bootty'),
                                         'config':request.POST.getlist('config'), 'pxe_adap': request.POST.getlist('pxe_adap'), 'cdets': request.POST.getlist('cdets'),
                                         'auto_logs':request.POST.getlist('automation_logs'), 'driver_ver':request.POST.getlist('driver_ver'),
                                         'auto_usage':request.POST.getlist('auto_usage'), 'result':request.POST.getlist('result'),
                                         'comments': request.POST.getlist('comments'), 'effort':request.POST.getlist('effort')}
            for tb in ucsm_testbed_f:
                if setup == tb.fi_ip + '_' + tb.server_type:
                    ucsm += 1
                    final_data[setup] = {'pk':ucsm_testbed_f.filter(id=tb.id), 'os': request.POST.getlist('os'), 'os_bootM': request.POST.getlist('os_bootm'),
                                         'os_bootT': request.POST.getlist('os_bootty'),
                                         'config': request.POST.getlist('config'),
                                         'pxe_adap': request.POST.getlist('pxe_adap'),
                                         'cdets': request.POST.getlist('cdets'),
                                         'auto_logs': request.POST.getlist('automation_logs'),
                                         'driver_ver': request.POST.getlist('driver_ver'),
                                         'auto_usage': request.POST.getlist('auto_usage'),
                                         'result': request.POST.getlist('result'),
                                         'comments': request.POST.getlist('comments'),
                                         'effort': request.POST.getlist('effort')}
        else:
            for tb in standalone_testbed_f:
                if re.match('(.*)-(.*)',setup):
                    stand += 1
                    final_data[setup+"("+str(pos)+")"] = {'pk':standalone_testbed_f.filter(id=tb.id), 'engineer':str(nname), 'os':request.POST.getlist('os'), 'os_bootM':request.POST.getlist('os_bootm'), 'os_bootT':request.POST.getlist('os_bootty'),
                                         'config':request.POST.getlist('config'), 'pxe_adap': request.POST.getlist('pxe_adap'), 'cdets': request.POST.getlist('cdets'),
                                         'auto_logs':request.POST.getlist('automation_logs'), 'driver_ver':request.POST.getlist('driver_ver'),
                                         'auto_usage':request.POST.getlist('auto_usage'), 'result':request.POST.getlist('result'),
                                         'comments': request.POST.getlist('comments'), 'effort':request.POST.getlist('effort')}
                    pos += 1
            for tb in ucsm_testbed_f:
                if setup == tb.fi_ip + '_' + tb.server_type:
                    ucsm += 1
                    final_data[setup+"("+str(pos)+")"] = {'pk':ucsm_testbed_f.filter(id=tb.id), 'os': request.POST.getlist('os'), 'os_bootM': request.POST.getlist('os_bootm'),
                                         'os_bootT': request.POST.getlist('os_bootty'),
                                         'config': request.POST.getlist('config'),
                                         'pxe_adap': request.POST.getlist('pxe_adap'),
                                         'cdets': request.POST.getlist('cdets'),
                                         'auto_logs': request.POST.getlist('automation_logs'),
                                         'driver_ver': request.POST.getlist('driver_ver'),
                                         'auto_usage': request.POST.getlist('auto_usage'),
                                         'result': request.POST.getlist('result'),
                                         'comments': request.POST.getlist('comments'),
                                         'effort': request.POST.getlist('effort')}
                    pos += 1

    pp(final_data)

    for s, d in final_data.iteritems():
        test_exec = TestExecution()
        if stand > 0:
            test_exec.testbed_stand = d.get('pk')[0]
        else:
            test_exec.testbed_stand = None
        if ucsm > 0:
            test_exec.testbed_ucsm = d.get('pk')[0]
        else:
            test_exec.testbed_ucsm = None
        try:
            test_exec.setup = s
            test_exec.os = d.get('os')[position]
            test_exec.os_bootM = d.get('os_bootM')[position]
            test_exec.os_bootT = d.get('os_bootT')[position]
            test_exec.config = d.get('config')[position]
            test_exec.pxe_adap = d.get('pxe_adap')[position]
            test_exec.cdets = d.get('cdets')[position]
            test_exec.auto_logs = d.get('auto_logs')[position]
            test_exec.auto_usage = d.get('auto_usage')[position]
            test_exec.driver_version = d.get('driver_ver')[position]
            test_exec.result = d.get('result')[position]
            test_exec.comments = d.get('comments')[position]
            test_exec.effort = d.get('effort')[position]
        except IndexError: break

        test_exec.save()
        position += 1
    return render(request, 'newhtml1.html', context1)


def change_pswd(request):
    return render(request, 'change_pswd.html')


def changepswd(request):
    # password = "changed"
    uname = request.session['uname']
    old = request.POST.get('old')
    new = request.POST.get('new')

    user_existence = Login.objects.get(user__startswith=str(uname))
    if user_existence.pswd == old:
        user_existence.pswd = new
    else:
        return HttpResponse("<h1>Exsisting password is not matched</h1>")
    user_existence.save()
    return redirect('/')


def history(request):
    uname = request.session['uname']
    user_existence = Login.objects.filter(user__startswith=str(uname))
    nname = ''
    for nn in user_existence:
        nname = nn.nickname

    standalone_testbed = StandaloneTestBedSetup.objects.filter(engineer__startswith=str(nname))
    ucsm_testbed = UcsmTestBedSetup.objects.filter(engineer__startswith=str(nname))
    execu = ''
    for b in standalone_testbed:
        execu = TestExecution.objects.filter(setup__startswith=b.cimc_ip)
        # print execu.os
    context = {
        'user_existence': user_existence,
        'standalone_testbed': standalone_testbed,
        'ucsm_testbed': ucsm_testbed,
        'execu': execu,
    }

    return render(request, 'history.html', context)

def export_data(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Report.xls"'
    fromdate = request.POST.get('fromDate')
    todate = request.POST.get('toDate')
    adap_inp = request.POST.get('adapter_filter')
    os_inp = request.POST.get('os_filter')
    release_inp = request.POST.get('release_filter')
    engineer_inp = request.POST.get('engineer_filter')
    # standalone1 = StandalonetesBedSetupFinal.objects.filter(event__range=[fromDate, toDate])
    TE = TestExecution.objects.filter(event__range=[fromdate,todate])
    print 'input of adapter is',adap_inp
    TB_engineer = StandaloneTestBedSetupFinal.objects.all().values_list('engineer')
    TB_cimc = StandaloneTestBedSetupFinal.objects.all().values_list('cimc_ip')
    cimc_li = []
    for i in  range(len(TB_engineer)):
        # print 'engineer is',TB_engineer[i],'type is',type(TB_engineer[i])
        en = str(TB_engineer[i]).lstrip('(u\'').rstrip('\',)')
        if en == engineer_inp:
            # nam = str(i).lstrip('[u\'').rstrip('\',')
            nam = str(TB_engineer[i]).lstrip('(u\'').rstrip('\',)')
            cimc =  str(TB_cimc[i]).lstrip('(u\'').rstrip('\',)')
            cimc_li.append(cimc)
            print 'hello',nam+'_'+cimc
    row1s = TE.values_list('setup','os','os_bootM','os_bootT','config','pxe_adap','cdets','auto_logs','auto_usage','driver_version','result','comments','effort','event')
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users')
    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['setup', 'os', 'os_boot Method', 'os_boot Type', 'config','pxe_adap','cdets','auto_logs','auto_usage','driver_version','result','comments','effort','Event']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()
    rows = TestExecution.objects.all().values_list('setup','os','os_bootM','os_bootT','config','pxe_adap','cdets','auto_logs','auto_usage','driver_version','result','comments','effort','event')
    # rows = User.objects.all().values_list('username', 'first_name', 'last_name', 'email')
    # for row in rows:
    for row in row1s:
        # row_num += 1
        rel1 = str(row[0]).split('-')[1]
        ip1 = str(row[0]).split('-')[0]
        if os_inp != 'OS':
            if (release_inp !='Release')and (adap_inp=='Adapter') and (engineer_inp=='Engineer'):
                print 'inside both release os'
                rel = str(row[0]).split('-')[1]
                if os_inp == row[1] and release_inp == rel:
                    row_num += 1
                    for col_num in range(len(row)):
                        ws.write(row_num, col_num, str(row[col_num]), font_style)
            elif (adap_inp !='Adapter') and (os_inp !='os') and (release_inp!='Release') and (engineer_inp=='Engineer'):
                print 'inside release os adapter'
                if os_inp == row[1] and release_inp ==rel1 and adap_inp in row[4]:
                    row_num += 1
                    for col_num in range(len(row)):
                        ws.write(row_num, col_num, str(row[col_num]), font_style)
            elif (adap_inp!='Adapter') and (release_inp=='Release')and (engineer_inp=='Engineer'):
                print 'inside os adapter'
                if os_inp==row[1] and adap_inp in row[4]:
                    row_num += 1
                    for col_num in range(len(row)):
                        ws.write(row_num, col_num, str(row[col_num]), font_style)
            elif release_inp != 'Release' and engineer_inp != 'Engineer' and os_inp != 'OS' and adap_inp=='Adapter':
                print 'inside engineer release os'
                for cimc in cimc_li:
                    if ip1 == cimc and release_inp==rel1 and os_inp== row[1]:
                        row_num += 1
                        for col_num in range(len(row)):
                            ws.write(row_num, col_num, str(row[col_num]), font_style)
            elif (os_inp !='OS') and (engineer_inp!='Engineer') and (adap_inp=='Adapter') and (release_inp=='Release'):
                print 'insid Engineer os'
                for cimc in cimc_li:
                    if ip1 == cimc and os_inp== row[1]:
                        row_num += 1
                        for col_num in range(len(row)):
                            ws.write(row_num, col_num, str(row[col_num]), font_style)
            elif release_inp != 'Release' and engineer_inp != 'Engineer' and os_inp != 'OS' and (adap_inp!='Adapter'):
                print 'inside Engineer release os adapter'
                for cimc in cimc_li:
                    if ip1 == cimc and release_inp==rel1 and os_inp== row[1] and adap_inp in row[4]:
                        row_num += 1
                        for col_num in range(len(row)):
                            ws.write(row_num, col_num, str(row[col_num]), font_style)

            elif os_inp == row[1]:
                print 'inside os'
                row_num += 1
                for col_num in range(len(row)):
                    ws.write(row_num, col_num, str(row[col_num]), font_style)

        elif engineer_inp!='Engineer':
            # for eng in cimc_li:
            ip = str(row[0]).split('-')[0]
            if release_inp!='Release' and engineer_inp!='Engineer' and adap_inp=='Adapter':
                print 'inside release engineer'
                for cimc in cimc_li:
                    if ip == cimc and release_inp == rel1:
                        row_num += 1
                        for col_num in range(len(row)):
                            ws.write(row_num, col_num, str(row[col_num]), font_style)
            elif release_inp!='Release' and engineer_inp!='Engineer' and adap_inp!='Adapter':
                print 'inside Engineer release adapter'
                for cimc in cimc_li:
                    if ip == cimc and release_inp == rel1 and adap_inp in row[4]:
                        row_num += 1
                        for col_num in range(len(row)):
                            ws.write(row_num, col_num, str(row[col_num]), font_style)
            elif release_inp=='Release' and adap_inp!='Adapter' and engineer_inp !='Engineer':
                print 'inside Engineer Adapter'
                for cimc in cimc_li:
                    if ip == cimc  and adap_inp in row[4]:
                        row_num += 1
                        for col_num in range(len(row)):
                            ws.write(row_num, col_num, str(row[col_num]), font_style)
            else:
                print 'inside Engineer'
                for cimc in cimc_li:
                    if ip == cimc:
                        row_num += 1
                        for col_num in range(len(row)):
                            ws.write(row_num, col_num, str(row[col_num]), font_style)
                # print 'eng is',eng
        elif release_inp != 'Release':
            rel = str(row[0]).split('-')[1]
            if (release_inp!='Release') and (adap_inp !='Adapter'):
                print 'inside release adapter'
                if release_inp == rel and adap_inp in row[4]:
                    row_num += 1
                    for col_num in range(len(row)):
                        ws.write(row_num, col_num, str(row[col_num]), font_style)

            elif release_inp == rel:
                print 'inside release'
                row_num += 1
                for col_num in range(len(row)):
                    ws.write(row_num, col_num, str(row[col_num]), font_style)
        elif adap_inp!='Adapter':
            print 'inside adapter'
            if adap_inp in row[4]:
                print 'inside adapter'
                row_num += 1
                for col_num in range(len(row)):
                    ws.write(row_num, col_num, str(row[col_num]), font_style)

        else:
            print 'inside else'
            row_num += 1
            for col_num in range(len(row)):
                ws.write(row_num, col_num, str(row[col_num]), font_style)


    wb.save(response)
    return response


def testmetrics(request):

    users = {}
    inserted = []
    fromDate = request.POST.get('fromDate')
    toDate = request.POST.get('toDate')
    team_filter = request.POST.get('team_filter')
    release_filter = request.POST.get('release_filter')
    os_filter = request.POST.get('os_filter')
    adapter_filter = request.POST.get('adapter_filter')
    eng_filter = request.POST.get('eng_filter')
    standalone = StandaloneTestBedSetup.objects.all()
    ucsm = UcsmTestBedSetup.objects.all()
    execute = TestExecution.objects.all()
    standalone1 = StandaloneTestBedSetupFinal.objects.filter(event__range=[fromDate, toDate])
    ucsm1 = UcsmTestBedSetupFinal.objects.filter(event__range=[fromDate, toDate])
    adapter_names = adapter_alias()
    osnames = os_names()
    users_all = Login.objects.all()
    # pp(standalone1)

    if team_filter == 'Rack OS-Compat-Standalone':
        for std in standalone1:
            if std.engineer not in inserted:
                inserted.append(std.engineer)
                query_testbed_engname = StandaloneTestBedSetup.objects.filter(engineer__startswith=std.engineer)
                # print "engname query is ",query_testbed_engname
                for a in query_testbed_engname:
                    # print a
                    if release_filter != 'release' and os_filter == 'OS' and eng_filter == 'Engineer':
                        if adapter_filter != 'Adapter':
                            if adapter_filter:
                                # print 'adapter filtered\n\n'
                                prim_key = []
                                print '\n'
                                adapter = a.adapter_name.split(',')
                                # print 'adapter content is'
                                # pp(adapter)
                                for adap in adapter:
                                    adap = str(adap).lstrip('[u\'').lstrip(' u\'').rstrip('\'').rstrip('\']')
                                    print 'adapters are', adap
                                    if re.match(str(adap), str(adapter_filter)):
                                        print 'matched for adapter filtering', adap, adapter_filter
                                        prim_key.append(a.cimc_ip)
                                for i in range(len(prim_key)):
                                    exe = TestExecution.objects.filter(
                                        setup__regex=a.cimc_ip + r'-' + str(release_filter) + r'+(\(\d\))?$')
                                    if exe:
                                        if std.engineer not in users.keys():
                                            users[std.engineer] = {a: exe}
                                        else:
                                            users.get(std.engineer)[a] = exe
                        elif release_filter != 'release':
                            print 'release filtered\n\n'
                            exe = TestExecution.objects.filter(
                                setup__regex=a.cimc_ip + r'-' + str(release_filter) + r'+(\(\d\))?$')
                            if exe:
                                # print exe
                                # for q in exe:
                                if std.engineer not in users.keys():
                                    users[std.engineer] = {a: exe}
                                else:
                                    users.get(std.engineer)[a] = exe
                            # pp(users)
                    if eng_filter != 'Engineer':
                        # print 'In eng_filter '
                        if str(a.engineer) == str(eng_filter):
                            # print a,str(eng_filter)+'matched engineer\n\n'
                            exe = TestExecution.objects.filter(setup__regex=a.cimc_ip + r'-' + str(release_filter) + r'+(\(\d\))?$')
                            if exe:
                                # print 'in exe loop', a
                                if std.engineer not in users.keys():
                                    users[std.engineer] = {a: exe}
                                else:
                                    users.get(std.engineer)[a] = exe
                                # pp(users)
                    if os_filter != 'OS':
                        # print 'os filtered\n\n'
                        if release_filter != 'release' and adapter_filter == 'Adapter':
                            exe = TestExecution.objects.filter(Q(setup__regex=a.cimc_ip+r'-'+str(release_filter)+r'+(\(\d\))?$') & Q(os__regex=r'^'+str(os_filter)+r'$'))
                            if exe:
                                for q in exe:
                                        s2 = re.search('(.*)-(.*)', q.setup)
                                        if str(a.cimc_ip) == str(s2.group(1)):
                                            if std.engineer not in users.keys():
                                                users[std.engineer] = {a: q}
                                            else:
                                                users.get(std.engineer)[a] = q
                                pp(users)
                        elif adapter_filter != 'Adapter' and release_filter == 'release':
                            pass
                        elif release_filter != 'release' and adapter_filter != 'Adapter':
                            if adapter_filter:
                                if eng_filter == 'Engineer':
                                    # print 'adapter filtered\n\n'
                                    prim_key = []
                                    print '\n'
                                    adapter = a.adapter_name.split(',')
                                    # print 'adapter content is'
                                    # pp(adapter)
                                    for adap in adapter:
                                        adap = str(adap).lstrip('[u\'').lstrip(' u\'').rstrip('\'').rstrip('\']')
                                        print adap
                                        if re.match(str(adap), str(adapter_filter)):
                                            print 'matched for adapter filtering', adap, adapter_filter, a
                                            prim_key.append(a.cimc_ip)
                                            pp(prim_key)
                                    # pp(prim_key)
                                    for key in prim_key:
                                        exe = TestExecution.objects.filter(Q(setup__regex=r'^' + key + r'-'+str(release_filter)+r'+(\(\d\))?$') & Q(os__regex=r'^'+str(os_filter)+r'$'))
                                        print 'exe done'
                                        if exe:
                                            print 'exe present ',exe,a
                                            for q in exe:
                                                print q.os
                                                if std.engineer not in users.keys():
                                                    users[std.engineer] = {a: q}
                                                else:
                                                    users.get(std.engineer)[a] = q
                                elif eng_filter != 'Engineer':
                                    # print 'adapter filtered\n\n'
                                    prim_key = []
                                    print '\n'
                                    adapter = a.adapter_name.split(',')
                                    # print 'adapter content is'
                                    # pp(adapter)
                                    for adap in adapter:
                                        adap = str(adap).lstrip('[u\'').lstrip(' u\'').rstrip('\'').rstrip('\']')
                                        print adap
                                        if re.match(str(adap), str(adapter_filter)):
                                            print 'matched for adapter filtering', adap, adapter_filter, a
                                            prim_key.append(a.cimc_ip)
                                            pp(prim_key)
                                    # pp(prim_key)
                                    for key in prim_key:
                                        if str(a.engineer) == str(eng_filter):
                                            print a.engineer
                                            exe = TestExecution.objects.filter(Q(
                                                setup__regex=r'^' + key + r'-' + str(release_filter) + r'+(\(\d\))?$') & Q(
                                                os__regex=r'^' + str(os_filter) + r'$'))
                                            print 'exe done'
                                            if exe:
                                                print 'exe present ', exe, a
                                                for q in exe:
                                                    print exe
                                                    if std.engineer not in users.keys():
                                                        users[std.engineer] = {a: q}
                                                    else:
                                                        users.get(std.engineer)[a] = q
                        else:
                            exe = TestExecution.objects.filter(os__regex=r'^'+str(os_filter)+r'$')
                            if exe:
                                # print 'exe present ', exe, a
                                for q in exe:
                                    # print q.os
                                    if std.engineer not in users.keys():
                                        users[std.engineer] = {a: q}
                                    else:
                                        users.get(std.engineer)[a] = q

                    if adapter_filter != 'Adapter' and release_filter == 'release' and os_filter == 'OS':
                        # print 'adapter filtered\n\n'
                        prim_key = []
                        adapter = a.adapter_name.split(',')
                        # print 'adapter content is'
                        # pp(adapter)
                        for adap in adapter:
                            adap = str(adap).lstrip('[u\'').lstrip(' u\'').rstrip('\'').rstrip('\']')
                            # print adap
                            if re.match(adap, adapter_filter):
                                # print 'matched for adapter filtering'
                                prim_key.append(std.cimc_ip)
                        # pp(prim_key)
                        for key in prim_key:
                            exe = TestExecution.objects.filter(setup__regex=r'^' + key + r'-(.*)$')
                            if exe:
                                # print exe
                                for q in exe:
                                    if std.engineer not in users.keys():
                                        users[std.engineer] = {a: q}
                                    else:
                                        users.get(std.engineer)[a] = q
                    # else:
                    #     exe = TestExecution.objects.filter(setup__regex=a.cimc_ip + r'-.*')
                    #     if std.engineer not in users.keys():
                    #         users[std.engineer] = {a: exe}
                    #     else:
                    #         users.get(std.engineer)[a] = exe
    elif team_filter == 'Rack OS-Compat-UCSM':
        for std in ucsm1:
            if std.engineer not in inserted:
                inserted.append(std.engineer)
                query_testbed_engname = UcsmTestBedSetup.objects.filter(engineer__startswith=std.engineer)
                # print "engname query is ",query_testbed_engname
                for a in query_testbed_engname:
                    if release_filter != 'release':
                        exe = TestExecution.objects.filter(setup__regex=a.fi_ip + r'-' + str(release_filter) + r'$')
                        if exe:
                            if std.engineer not in users.keys():
                                users[std.engineer] = {a: exe}
                            else:
                                users.get(std.engineer)[a] = exe
                    if os_filter != 'OS':
                        exe = TestExecution.objects.filter(setup__regex=a.fi_ip+r'-'+str(release_filter)+r'$', os__icontains=str(os_filter))
                        if exe:
                            if std.engineer not in users.keys():
                                users[std.engineer] = {a: exe}
                            else:
                                users.get(std.engineer)[a] = exe
                                if adapter_filter != 'Adapter':
                                    print 'adapter filtered\n\n'
                                    prim_key = []
                                    adapter = a.adapter_name.split(',')
                                    for adap in adapter:
                                        # print adap
                                        if re.match(adap, adapter_filter):
                                            prim_key.append(std.cimc_ip)
                                    # pp(prim_key)
                                    for key in prim_key:
                                        exe = TestExecution.objects.filter(setup__regex=r'^' + key + r'-(.*)$')
                                        if exe:
                                            print exe
                                            if std.engineer not in users.keys():
                                                users[std.engineer] = {a: exe}
                                            else:
                                                users.get(std.engineer)[a] = exe
                    # else:
                    #     exe = TestExecution.objects.filter(setup__regex=a.fi_ip + r'-.*')
                    #     if std.engineer not in users.keys():
                    #         users[std.engineer] = {a: exe}
                    #     else:
                    #         users.get(std.engineer)[a] = exe
    # elif team_filter == 'All Teams':
    #     for std in standalone1:
    #         if std.engineer not in inserted:
    #             # inserted.append(std.engineer)
    #             query_testbed_engname = StandaloneTestBedSetup.objects.filter(engineer__startswith=std.engineer)
    #             # print "engname query is ",query_testbed_engname
    #             for a in query_testbed_engname:
    #                 if release_filter != 'release' and os_filter != 'OS':
    #                     exe = TestExecution.objects.filter(setup__regex=a.cimc_ip+r'-'+str(release_filter)+r'$', os__icontains=str(os_filter))
    #                     if exe:
    #                         if std.engineer not in users.keys():
    #                             users[std.engineer] = {a: exe}
    #                         else:
    #                             users.get(std.engineer)[a] = exe
    #                 else:
    #                     exe = TestExecution.objects.filter(setup__regex=a.cimc_ip + r'-.*')
    #                     if std.engineer not in users.keys():
    #                         users[std.engineer] = {a: exe}
    #                     else:
    #                         users.get(std.engineer)[a] = exe
    #
    #     for std in ucsm1:
    #         if std.engineer not in inserted:
    #             # inserted.append(std.engineer)
    #             query_testbed_engname = UcsmTestBedSetup.objects.filter(engineer__startswith=std.engineer)
    #             # print "engname query is ",query_testbed_engname
    #             for a in query_testbed_engname:
    #                 if release_filter != 'release' and os_filter != 'OS':
    #                     exe = TestExecution.objects.filter(setup__regex=a.fi_ip+r'-'+str(release_filter)+r'$', os__icontains=str(os_filter))
    #                     if exe:
    #                         if std.engineer not in users.keys():
    #                             users[std.engineer] = {a: exe}
    #                         else:
    #                             users.get(std.engineer)[a] = exe
    #                 else:
    #                     exe = TestExecution.objects.filter(setup__regex=a.fi_ip + r'-.*')
    #                     if std.engineer not in users.keys():
    #                         users[std.engineer] = {a: exe}
    #                     else:
    #                         users.get(std.engineer)[a] = exe
    # elif team_filter == 'All Teams':
    #     for std in standalone1:
    #         if std.engineer not in inserted:
    #             # inserted.append(std.engineer)
    #             query_testbed_engname = StandaloneTestBedSetup.objects.filter(engineer__startswith=std.engineer)
    #             # print "engname query is ",query_testbed_engname
    #             for a in query_testbed_engname:
    #                 if release_filter != 'release' and os_filter == 'OS':
    #                     print 'first condition\n\n'
    #                     exe = TestExecution.objects.filter(setup__regex=a.cimc_ip+r'-'+str(release_filter)+r'$')
    #                 elif os_filter != 'OS' and release_filter != 'release':
    #                     print 'got condition\n\n'
    #                     exe = TestExecution.objects.filter(setup__regex=a.cimc_ip + r'-' + str(release_filter) + r'$', os__icontains=str(os_filter))
    #                 if exe:
    #                     if std.engineer not in users.keys():
    #                         users[std.engineer] = {a: exe}
    #                     else:
    #                         users.get(std.engineer)[a] = exe
    #                 else:
    #                     exe = TestExecution.objects.filter(setup__regex=a.cimc_ip + r'-.*')
    #                     if std.engineer not in users.keys():
    #                         users[std.engineer] = {a: exe}
    #                     else:
    #                         users.get(std.engineer)[a] = exe

        # for std in ucsm1:
        #     if std.engineer not in inserted:
        #         # inserted.append(std.engineer)
        #         query_testbed_engname = UcsmTestBedSetup.objects.filter(engineer__startswith=std.engineer)
        #         # print "engname query is ",query_testbed_engname
        #         for a in query_testbed_engname:
        #             if release_filter != 'release':
        #                 exe = TestExecution.objects.filter(setup__regex=a.fi_ip+r'-'+str(release_filter)+r'$')
        #                 if exe:
        #                     if std.engineer not in users.keys():
        #                         users[std.engineer] = {a: exe}
        #                     else:
        #                         users.get(std.engineer)[a] = exe
        #             else:
        #                 exe = TestExecution.objects.filter(setup__regex=a.fi_ip + r'-.*')
        #                 if std.engineer not in users.keys():
        #                     users[std.engineer] = {a: exe}
        #                 else:
        #                     users.get(std.engineer)[a] = exe
    pp(users)
    context = {
        'standalone': standalone,
        'ucsm': ucsm,
        'execute': execute,
        'users': users,
        'standalone1': standalone1,
        'ucsm1': ucsm1,
        'adapter_names': adapter_names,
        'osnames': osnames,
        'users_all': users_all,
    }
    return render(request, 'filter.html', context)