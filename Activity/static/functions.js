/**
 * Created by pyogaraj on 6/6/2017.
 */
 var a=0;
 var b=0;
 var c=0;
 var d=0;
 var f=0;
// var arr_adap = ['Adapter','1225'];
function testbed_validate(){
	//alert("hi");
	var v = document.getElementById("teamsel").value;
	if (v == "Team"){alert("Please Select Team");}
}
function va(){
	
	var v = document.getElementById("execsel").value;
	if (v == "Select Release"){alert("Please Select Release");}
}
 function addInp(){

  var inp = document.getElementById("teamsel1").value;
    if(inp == "Log out"){
    window.location="/";
       }
       return false;
  }
function preview(){
    document.getElementById("myForm1").submit();
}
function testsub(){
     document.getElementById("myForm").submit();

}
function testm(){
    document.getElementById("test_met").submit();
}
function tb_modify(){
     document.getElementById("myForm2").submit();

}
function send(){
	document.getElementById("myForm1").submit();
	
	return false;
}
function troubleshoot(){


    var trdiv = document.getElementById("testedselect_troubleshoot");
    var sel = document.getElementById("testselect_troubleshoot").value;

     var div_troubleshoot = document.createElement("div");
     div_troubleshoot.className = "troubleshootclass";

     var activitylabel_troubleshoot = document.createElement("input");
	    activitylabel_troubleshoot.value = sel;
		activitylabel_troubleshoot.name = "actlabel";

		activitylabel_troubleshoot.className = "actlabel";
		activitylabel_troubleshoot.readOnly = "true";

		div_troubleshoot.appendChild(activitylabel_troubleshoot);

      var troubleshoot_table = document.createElement("table");
      var row1 = document.createElement("tr");
      var row1_td1 = document.createElement("td");
      var row1_inp1 = document.createElement("textarea");
      row1_inp1.id = "textareaid";
      row1_inp1.name = "textareaname";

      row1_td1.appendChild(row1_inp1);
      row1.appendChild(row1_td1);
      troubleshoot_table.appendChild(row1);

      div_troubleshoot.appendChild(troubleshoot_table);
      trdiv.appendChild(div_troubleshoot);

}

var r = null;
function ret_sel(id){
    //alert(document.getElementsByClassName(id)[0].innerHTML);

    r = document.getElementsByClassName(id)[0].innerHTML;
}

function firware_review(id){


    var trdiv = document.getElementById("FW_rev");
    var sel = document.getElementById("fwReview").value;
    var activity = r;

     var div_troubleshoot = document.createElement("div");
     div_troubleshoot.className = "fwclass";
     div_troubleshoot.id = "fwreview";

     var activitylabel_troubleshoot = document.createElement("input");
	    activitylabel_troubleshoot.value = sel + "-" + activity;
		activitylabel_troubleshoot.name = "actlabel";

		activitylabel_troubleshoot.className = "actlabel";
		activitylabel_troubleshoot.readOnly = "true";

		div_troubleshoot.appendChild(activitylabel_troubleshoot);

      var troubleshoot_table = document.createElement("table");
      var row1 = document.createElement("tr");
      var row1_td1 = document.createElement("td");
      var row1_inp1 = document.createElement("textarea");
      row1_inp1.id = "textareaid";
      row1_inp1.name = "textareaname";

      var row2 = document.createElement("tr");
      var row2_td1 = document.createElement("td");
      var row2_inp1 = document.createElement("input")
      row2_inp1.id = "effortid";
      row2_inp1.placeholder = "Effort in HRS";
      row2_inp1.type = "number";
      row2_inp1.name = "efforname";

      row1_td1.appendChild(row1_inp1);
      row2_td1.appendChild(row2_inp1);
      row1.appendChild(row1_td1);
      row2.appendChild(row2_td1);
      troubleshoot_table.appendChild(row1);
      troubleshoot_table.appendChild(row2);

      div_troubleshoot.appendChild(troubleshoot_table);
      trdiv.appendChild(div_troubleshoot);

}

function validate(){
	//alert("b is"+b)
    var flag =0;
		tmp_name = "os_name"+b;
		var res = tmp_name.split(/\D/);
	//	alert("res is"+res[7]);
     //  var tmpname = b;
      // tmp_arr.push(tmpname);
    var driver_version = document.getElementsByClassName("Driver_version")[0].value;
    var pxeadapter = document.getElementsByClassName("pxeadapinp")[0].value;
    var automation_input = document.getElementsByClassName("auto_sel")[0].value;
     var adap_drop  = document.getElementsByClassName("Boot_type_class")[0].value;
     var link_logs = document.getElementsByClassName("Link_Logs")[0].value;
     var os = document.getElementsByClassName("os_name")[0].value;



       for(var i=0;i<=b;i++){
          var na =  document.getElementsByName("os_name"+res[7])[0].value;
          if(na == "OS"){

        alert("Please Select OS....");
        flag = flag+1;

        }
       }


    for(var i=0;i<=b;i++){
      var na =  document.getElementsByName("Boot_Type"+res[7])[0].value;
      var na1 = document.getElementsByName("Pxe_adapter"+res[7])[0].value;
   if((na == "PXE" && na1 == "")){
            alert("Please Enter the Pxe Adapter...");
        flag = flag +1;
    }
     }
     for(var i=0;i<=b;i++){
     var na =  document.getElementsByName("Boot_Type"+res[7])[0].value;

    if(na == "Boot Method"){

        alert("Please select the Boot Method...");
        flag = flag +1;
    }
    }
    for(var i=0;i<=b;i++){
    var na =  document.getElementsByName("auto_type"+res[7])[0].value;
    var na1 =  document.getElementsByName("Link_Automation"+res[7])[0].value;

    if(((na=="CAS")||(na=="IAS"))&& (na1 =="")){
         alert("Please Enter the Link for the logs...");

        flag = flag+1;
    }
    }


    if(flag ==0) {
    document.getElementById("myForm1").submit();
    }
    return false;
    }

function createSelect(){

    var rel = document.getElementById("execseldiv");
     var drop2 = document.getElementById("testedselect");
    rel.style.display = "block";
    drop2.style.display = "block";


    return false;
}
function testbedselect(){
    var drop1 = document.getElementById("testdbedsetup");

    drop1.style.display = "block";

    return false;

}
function troubleshootselect(){

    var testbed =  document.getElementById("testedselect_troubleshoot");
    testbed.style.display = "block";

    return false;

}

function closemodal(id){

    var tmp_id = id;

    var strid = tmp_id.split(/\D/);
     var modal = document.getElementById("mod"+strid[4]);
        document.getElementById("mod"+strid[4]).style.display = "none";
     return false;
}

// When the user clicks on <span> (x), close the modal


// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    var modal = document.getElementById("myModal");
    if (event.target == modal) {

        modal.style.display = "block";
    }
    return false
}

function openModal(name){


//	var y = document.getElementById("myUcsmModal");
	var team = document.getElementById("teamsel").value;
	if((team == "Rack OS-Compat-Standalone")){

    var tmp_name = name;
    var res = tmp_name.split(/\D/);
    var na =  document.getElementsByName("Adapter"+res[7])[0];
    var x = document.getElementById("mod"+res[7]);
	x.style.display = "block";
	document.getElementById('teamsel').style.borderColor = "black";
	}
 if (team == "Rack OS-Compat-UCSM"){

    var tmp_name = name;
    var res = tmp_name.split(/\D/);
     var y = document.getElementById("mod"+res[12]);


	y.style.display = "block";
	document.getElementById('teamsel').style.borderColor = "black";


	}


	return false;
}

function fwreviewselect(){

    var fw_select =  document.getElementById("FW_rev");
    fw_select.style.display = "block";

    return false;

}

function selfunc(name){

	f = f+1;
    var tmp_name = name;
    var res = tmp_name.split(/\D/);

    var arr_boot = ['SAN','ISCSI','LOCAL','NA'];
	var sel = document.getElementById("sel"+res[3]);
	var ucsm_sel  = document.getElementById("ucsm_sel");
	 var team = document.getElementById("teamsel").value;
	
    var sel1 = document.getElementById("selid"+res[3]).value;
	var div = document.createElement("div");
    div.id = "Standalone_modal";
	div.className = "st_mod"+f;

    var ucdiv = document.createElement("div");
    ucdiv.id = "ucs";
    var ftable =  document.createElement("table");
	ftable.id = "ftab";

	var ucsmtable = document.createElement("table");
	ucsmtable.id = "ucsmtab";

    var row1 = document.createElement("tr");
    var row1_ucsmmodal = document.createElement("tr");

    var row1_td1 = document.createElement("td");
    var row1_td1_ucsm = document.createElement("td");
    var row1_inp1  = document.createElement("input");
//    row1_inp1.disabled = "true";
    row1_inp1.id ="Adapter";
	row1_inp1.name = "Adapter"+res[3];
    row1_inp1.value = document.getElementById("selid"+res[3]).value;
	row1_td1.appendChild(row1_inp1);
    row1.appendChild(row1_td1);

    var row1_inp1_ucsm  = document.createElement("input");
    row1_inp1_ucsm.id = "ucsmadap";
    row1_inp1_ucsm.name = "ucsm_adapter"+res[3];
    row1_inp1_ucsm.value = document.getElementById("selid"+res[3]).value;
    row1_td1_ucsm.appendChild(row1_inp1_ucsm);
    row1_ucsmmodal.appendChild(row1_td1_ucsm);

     var row1_td2 = document.createElement("td");
     var row1_td2_ucsm = document.createElement("td");

    var row1_inp2  = document.createElement("input");
   	row1_inp2.placeholder = "Slot";
	row1_inp2.name = "slot"+res[3];
    row1_inp2.id ="slot";
	row1_td2.appendChild(row1_inp2);
    row1.appendChild(row1_td2);

    var row1_inp2_ucsm = document.createElement("input");
    row1_inp2_ucsm.placeholder = "Slot";
    row1_inp2_ucsm.name = "ucsmslot"+res[3];
    row1_inp2_ucsm.id = "ucsslot";
    row1_td2_ucsm.appendChild(row1_inp2_ucsm);
    row1_ucsmmodal.appendChild(row1_td2_ucsm);


     var row1_td3 = document.createElement("td");
    var row1_inp3  = document.createElement("input");
	row1_inp3.placeholder = "Firmware";
	row1_inp3.name = "Firmware"+res[3];
    row1_inp3.id ="Firmware";
	row1_td3.appendChild(row1_inp3);
    row1.appendChild(row1_td3);

    var row1_td3_ucsm = document.createElement("td");
    var row1_inp3_ucsm = document.createElement("input");
    row1_inp3_ucsm.placeholder = "Firmware";
    row1_inp3_ucsm.name = "ucsfirmware"+res[3];
    row1_inp3_ucsm.id = "ucsfw";
    row1_td3_ucsm.appendChild(row1_inp3_ucsm);
    row1_ucsmmodal.appendChild(row1_td3_ucsm);

      var row1_td4 = document.createElement("td");
      var row1_inp4 = document.createElement("select");
        row1_inp4.id ="boot";
		row1_inp4.name = "boot"+res[3];

               for(i=0;i<arr_boot.length;i++){
              var option = document.createElement("option");
               option.text = arr_boot[i];
               option.value = arr_boot[i];
               row1_inp4.appendChild(option);

           }
	row1_td4.appendChild(row1_inp4);
    row1.appendChild(row1_td4);

     var row1_td4_ucsm = document.createElement("td");
     var row1_inp4_ucsm = document.createElement("select");
     row1_inp4_ucsm.id = "ucsboot";
     row1_inp4_ucsm.name = "ucsboot"+res[3];
           for(i=0;i<arr_boot.length;i++){
              var option = document.createElement("option");
               option.text = arr_boot[i];
               option.value = arr_boot[i];
               row1_inp4_ucsm.appendChild(option);

           }
           row1_td4_ucsm.appendChild(row1_inp4_ucsm);
           row1_ucsmmodal.appendChild(row1_td4_ucsm);

    var row1_td5 = document.createElement("td");
    var row1_inp5  = document.createElement("input");
	row1_inp5.placeholder = "Bios/Bootcode";
	row1_inp5.name = "Bootcode"+res[3];
    row1_inp5.id ="BootCode";
	row1_td5.appendChild(row1_inp5);
    row1.appendChild(row1_td5);
	
	var row1_td6 = document.createElement("td");
	var row1_inp6 = document.createElement("span");
		row1_inp6.innerHTML = "&times;";
		row1_inp6.className = "del";
		row1_inp6.id = "del"+f;
		row1_inp6.setAttribute('onclick','deleteModal(this.id)');
		row1_td6.appendChild(row1_inp6);
	//	row1.appendChild(row1_td6);
		
     var row1_td5_ucsm = document.createElement("td");
    var row1_inp5_ucsm  = document.createElement("input");
	row1_inp5_ucsm.placeholder = "Bios/Bootcode";
	row1_inp5_ucsm.name = "ucsbios"+res[3];
    row1_inp5_ucsm.id ="ucsboot";
	row1_td5_ucsm.appendChild(row1_inp5_ucsm);
    row1_ucsmmodal.appendChild(row1_td5_ucsm);

     ftable.appendChild(row1);
    ucsmtable.appendChild(row1_ucsmmodal);
    div.appendChild(row1);
     if(team == "Rack OS-Compat-Standalone"){
    div.appendChild(ftable);
     sel.appendChild(div);
        }

      if(team == "Rack OS-Compat-UCSM"){
      ucdiv.appendChild(ucsmtable);
      sel.appendChild(ucdiv);

      }
     return false;

}

    function displaystandalonerow(name){

        var tmp_name = name;
        var res = tmp_name.split(/\D/);
        var team = document.getElementById("teamsel").value;
        var  div_standalone_row2 = document.getElementById("row2_id"+res[4]);

        var testbed_class = document.getElementsByClassName("testbedclass"+res[4])[0];
        testbed_class.style.height = "140px";
        div_standalone_row2.style.marginTop = "8px";
        div_standalone_row2.style.display = "block";


}

    function displayucsmrow(name){

        var tmp_name = name;
        var res = tmp_name.split(/\D/);
     var team = document.getElementById("teamsel").value;

    var ucsm_row2 =document.getElementById("ucsm_row2_id"+res[4]);
    var ucsmtestbed = document.getElementsByClassName("Ucsmtestbedclass"+res[4])[0];

    ucsmtestbed.style.height = "150px";
    ucsmtestbed.style.width = "1080px";
    ucsm_row2.style.display = "block";



}
  function testbedfunc(){
        var x = document.getElementById("testbed").value;
        var y = document.getElementById("testbed");
        var mdiv = document.getElementById("maindiv");

        var team = document.getElementById("teamsel").value;

        c=c+1;
        d=c-1-d;
	//	alert("c is"+c);
		//alert("d is"+d);
//        d=d-1-c;
             var divid = document.getElementById("testdbedsetup");
      //  var div_but = document.createElement("div");
        var div_standalone = document.createElement("div");
        div_standalone.id = "row1_id"+d;
        div_standalone.name = "testbed_div";
        var div_standalone_row2 = document.createElement("div");
        div_standalone_row2.id = "row2_id"+d;

        var div_ucsm = document.createElement("div");
        var div_ucsm_row2 = document.createElement("div");
        div_ucsm_row2.id = "ucsm_row2_id"+d;

        div_ucsm.className = "Ucsmtestbedclass"+d;
        div_ucsm.name = "testbed_div";
        div_ucsm.style.width = "900px";
        div_ucsm.style.height = "90px";
        div_ucsm.style.marginTop = "10px";
        div_ucsm.style.marginLeft = "-5px";
        div_ucsm.style.border = "groove";

             div_standalone.className = "testbedclass"+d;
             div_standalone.style.width = "900px";
             div_standalone.style.height = "90px";
             div_standalone.style.border = "groove";
             div_standalone.style.marginTop = "10px";


	    var modaldiv = document.createElement("div");
        modaldiv.id = "mod"+d;
        modaldiv.className = "modal";
        var modalcontent = document.createElement("div");
        modalcontent.className = "modal-content";
        var modalheader = document.createElement("div");
        modalheader.className = "modal-header";
        var span = document.createElement("span");
        span.className = "close";
        var closebutton = document.createElement("button");
        closebutton.id = "save"+d;
        closebutton.className = "save";
        closebutton.innerHTML = "SAVE";
        closebutton.setAttribute('onclick','closemodal(this.id)');
		
		 var exitbutton = document.createElement("button");
        exitbutton.id = "save"+d;
        exitbutton.className = "save";
        exitbutton.innerHTML = "EXIT";
        exitbutton.setAttribute('onclick','closemodal(this.id)');
        span.appendChild(exitbutton);
		
        span.appendChild(closebutton);
        span.appendChild(closebutton);
        modalheader.appendChild(span);
        var y = document.createElement("H3");
         var t = document.createTextNode("Adapter Details "+team);
             y.appendChild(t);
         modalheader.appendChild(y);
        var modalbody = document.createElement("div");
        modalbody.className = "modal-body";

        var modalsel = document.createElement("div");
        modalsel.id = "sel"+d;
        modalsel.name = "sel"+d;


         var sel_inp = document.createElement("select");
            sel_inp.id = "selid"+d;
            sel_inp.name = "sel"+d
             sel_inp.setAttribute("onchange","selfunc(this.name)");
			  for(i=0;i<arr_adap.length;i++){
               var option = document.createElement("option");
               option.text = arr_adap[i];
               option.value = arr_adap[i];
               sel_inp.appendChild(option);
               }
            modalsel.appendChild(sel_inp);
//        modaldiv.style.width = "800px";
//        modaldiv.style.height = "500px";
//        modaldiv.style.backgroundColor = "yellow";
        modalbody.appendChild(modalsel);
        modalcontent.appendChild(modalheader);
        modalbody.appendChild(modalsel);
        modalcontent.appendChild(modalbody);

        modaldiv.appendChild(modalcontent);

         var arr_server = ['Server','C460-M4','C22-M3','C24-M3','C220-M3','C240-M3','C220-M4','C240-M4','C3X60-M3','C3X60-M4','C480-M5','C240-M5','C220-M5'];
        var arr_upgradeprocess = ['F/W Upgrade Process','Mapping vdvd','sentinnel'];
        var arr_discovery = ['Discovery Methods','Single Wire management','Dual Wire Management'];

        var activitylabel = document.createElement("input");
			activitylabel.value = team +"-" +d;
			activitylabel.name = "actlabel";
			activitylabel.className = "actlabel";
			activitylabel.readOnly = "true";
			div_standalone.appendChild(activitylabel);

           var testbedtable = document.createElement("table");
                testbedtable.id = "testbed";
             var ucsm_activitylabel = document.createElement("input");
			ucsm_activitylabel.value = team +"-" +d;
			ucsm_activitylabel.name = "actlabel";
			ucsm_activitylabel.className = "actlabel";
			ucsm_activitylabel.readOnly = "true";
			 div_ucsm.appendChild(ucsm_activitylabel);

          var row1 = document.createElement("tr");
          var row1_ucsm = document.createElement("tr");
          var row2_ucsm = document.createElement("tr");
          var row3_ucsm = document.createElement("tr");


          var row1_ucsm_td1 = document.createElement("td");
          row1_ucsm_td1.id = "Fi_ip_ucsm";

          var row1_ucsm_td2 = document.createElement("td");
          row1_ucsm_td2.id = "Fi_Firmware";

          var row1_ucsm_td3 = document.createElement("td");
          row1_ucsm_td3.id = "server_ucsm";

          var row1_ucsm_td4 = document.createElement("td");
          row1_ucsm_td4.id = "server_num_ucsm";

          var row1_ucsm_td5 = document.createElement("td");
          row1_ucsm_td5.id = "loaducsm";

          var row1_ucsm_td6 = document.createElement("td");
          row1_ucsm_td6.id = "enterucsm";

          var row1_ucsm_td7 = document.createElement("td");
          row1_ucsm_td7.id = "ucsmtestbedeffort";

          var row2_ucsm_td1 = document.createElement("td");
          row2_ucsm_td1.id = "cimc_version";

           var row2_ucsm_td2 = document.createElement("td");
          row2_ucsm_td2.id = "bios_version";

           var row2_ucsm_td3 = document.createElement("td");
            row2_ucsm_td3.id = "adapter";

            var row2_ucsm_td4 = document.createElement("td");
            row2_ucsm_td4.id = "discovery_method";

          var row1_td1 = document.createElement("td");
          row1_td1.id = "cimc_ip_standalone";

          var row1_td2 = document.createElement("td");
          row1_td2.id = "Cimc_Password"

          var row1_td3 = document.createElement("td");
          row1_td3.id = "loadcimcdetail"

          var row1_td4 = document.createElement("td");
          row1_td4.id = "entercimcdetail"

          var row1_td5 = document.createElement("td");
          row1_td5.id = "Testbedeffort";

          var row2 = document.createElement("tr");
          var row2_td2 = document.createElement("td");
          row2_td2.id = "server_standalone";
          var row2_td3 = document.createElement("td");
          row2_td3.id = "cimcbios_standalone_id";
          var row2_td4 = document.createElement("td");
          row2_td4.id = "adapter_standalone_id";
           var row2_td5 = document.createElement("td");
          row2_td5.id = "FW_upgradeprocess_id";



            var row1_inp1  = document.createElement("input");
		    row1_inp1.placeholder = "CIMC IP";
			row1_inp1.name = "CIMC";
			row1_inp1.id = "cimc_standalone";
			row1_td1.appendChild(row1_inp1);

			var row1_inp2 = document.createElement("input");
			row1_inp2.placeholder = "CIMC Password";
			row1_inp2.name = "cimc_password";
			row1_inp2.style.marginLeft = "5px";
			row1_inp2.id = "cimcpass";
			row1_td2.appendChild(row1_inp2);

			 var row1_inp3 = document.createElement("button");
             row1_inp3.id = "load_cimc";
			 row1_inp3.name = "load_detail";
			// row1_inp3.disabled = "true";
			 row1_inp3.background = "#d9d9d9";
			 row1_inp3.className = "load"+d;
			 row1_inp3.style.marginLeft = "1px";
			 row1_inp3.style.marginBottom = "2px";
			 row1_inp3.style.width = "150px";

             row1_inp3.setAttribute('onclick', 'displaystandalonerow(this.className)');
			 row1_inp3.innerHTML = "Load Cimc Detail";
             row1_td3.appendChild(row1_inp3);


             var row1_inp4 = document.createElement("button");
             row1_inp4.id = "enter_cimc";
			 row1_inp4.name = "enter_detail";
			 row1_inp4.className = "load"+d;
			 row1_inp4.style.marginLeft = "1px";
			 row1_inp4.style.marginBottom = "2px";
			 row1_inp4.style.width = "150px";

             row1_inp4.setAttribute('onclick', 'displaystandalonerow(this.className)');
			 row1_inp4.innerHTML = "Enter Cimc Detail";
             row1_td4.appendChild(row1_inp4);

             var row1_inp5 = document.createElement("input");
			 row1_inp5.type = "number";
             row1_inp5.name = "standalone_effort";
             row1_inp5.id = "effort_testbed_standalone";
             row1_inp5.placeholder = "Effort in Hrs";
             row1_td5.appendChild(row1_inp5);

			var row1_ucsm_inp1  = document.createElement("input");
			row1_ucsm_inp1.placeholder = "FI Ip";
			row1_ucsm_inp1.name = "FI Ip";
			row1_ucsm_inp1.id = "Fi_ip";
			row1_ucsm_td1.appendChild(row1_ucsm_inp1);

			var row1_ucsm_inp2 = document.createElement("input");
			row1_ucsm_inp2.placeholder = "FI Firmware";
			row1_ucsm_inp2.name = "FI Firmware";
			row1_ucsm_inp2.id = "Fi_FW";
			row1_ucsm_td2.appendChild(row1_ucsm_inp2);

			var row1_ucsm_inp3 = document.createElement("select");
			row1_ucsm_inp3.name = "Ucsm_servername";
			row1_ucsm_inp3.id = "ucsm_servername";
			  for(i=0;i<arr_server.length;i++){
               var option = document.createElement("option");
               option.text = arr_server[i];
               option.value = arr_server[i];
               row1_ucsm_inp3.appendChild(option);
               }
               row1_ucsm_td3.appendChild(row1_ucsm_inp3);

            var row1_ucsm_inp4 = document.createElement("input");
			row1_ucsm_inp4.placeholder = "Server Number";
			row1_ucsm_inp4.name = "server_num";
			row1_ucsm_inp4.id = "server_num";
			row1_ucsm_td4.appendChild(row1_ucsm_inp4);


            var row1_ucsm_inp5 = document.createElement("button");
            row1_ucsm_inp5.id = "load_ucsm";
            row1_ucsm_inp5.name = "load_ucsmdetail";
		//	row1_ucsm_inp5.disabled = "true";
            row1_ucsm_inp5.className = "ucsm"+d;
            row1_ucsm_inp5.style.marginLeft = "1px";
            row1_ucsm_inp5.style.marginBottom = "2px";
            row1_ucsm_inp5.style.width = "150px";
            row1_ucsm_inp5.setAttribute('onclick', 'displayucsmrow(this.className)');
            row1_ucsm_inp5.innerHTML = "Load UCSM Detail";
            row1_ucsm_td5.appendChild(row1_ucsm_inp5);

            var row1_ucsm_inp6 = document.createElement("button");
             row1_ucsm_inp6.id = "enter_ucsm";
            row1_ucsm_inp6.name = "enter_ucsmdetail";
            row1_ucsm_inp6.className = "ucsm"+d;
            row1_ucsm_inp6.style.marginLeft = "-1px";
            row1_ucsm_inp6.style.marginBottom = "2px";
            row1_ucsm_inp6.style.width = "150px";
            row1_ucsm_inp6.setAttribute('onclick', 'displayucsmrow(this.className)');
            row1_ucsm_inp6.innerHTML = "Enter UCSM Detail";
            row1_ucsm_td6.appendChild(row1_ucsm_inp6);

            var row1_ucsm_inp7 = document.createElement("input");
			row1_ucsm_inp7.type = "number";
			
            row1_ucsm_inp7.id = "ucsm_effort";
            row1_ucsm_inp7.name = "ucsmeffort";
            row1_ucsm_inp7.placeholder = "Effort in Hrs";
            row1_ucsm_td7.appendChild(row1_ucsm_inp7);

			var row2_ucsm_inp1  = document.createElement("input");
			row2_ucsm_inp1.placeholder = "CIMC version";
			row2_ucsm_inp1.name = "CIMC_Version";
			row2_ucsm_inp1.id = "ucsm_cimc";
			row2_ucsm_td1.appendChild(row2_ucsm_inp1);

			var row2_ucsm_inp2  = document.createElement("input");
			row2_ucsm_inp2.placeholder = "BIOS version";
			row2_ucsm_inp2.name = "BIOS_Version";
			row2_ucsm_inp2.id = "ucsm_bios";
			row2_ucsm_td2.appendChild(row2_ucsm_inp2);

			var row2_ucsm_inp3 = document.createElement("button");
             row2_ucsm_inp3.id = "ucsm_adapter";
			 row2_ucsm_inp3.name = "ucsm_Adapter"+d;
             row2_ucsm_inp3.style.width = "120px";
             row2_ucsm_inp3.setAttribute('onclick', 'openModal(this.name)');
			 row2_ucsm_inp3.innerHTML = "Adapter";
             row2_ucsm_td3.appendChild(row2_ucsm_inp3);


            var row2_ucsm_inp4 = document.createElement("select");
			row2_ucsm_inp4.name = "Discovery_method";
			row2_ucsm_inp4.id = "Discovery_method";
			row2_ucsm_inp4.style.marginRight = "50px";
			  for(i=0;i<arr_discovery.length;i++){
               var option = document.createElement("option");
               option.text = arr_discovery[i];
               option.value = arr_discovery[i];
               row2_ucsm_inp4.appendChild(option);
               }
               row2_ucsm_td4.appendChild(row2_ucsm_inp4);

			 var row2_inp2  = document.createElement("select");
            row2_inp2.id = "ucsm_server";
            row2_inp2.name = "Server_name";
                for(i=0;i<arr_server.length;i++){
               var option = document.createElement("option");
               option.text = arr_server[i];
               option.value = arr_server[i];
               row2_inp2.appendChild(option);
               }
            row2_td2.appendChild(row2_inp2);

            var row2_inp3  = document.createElement("input");
		    row2_inp3.placeholder = "CIMC BIOS";
			row2_inp3.name = "CIMC_BIOS";
			row2_inp3.id = "cimcbios_standalone";
			row2_td3.appendChild(row2_inp3);

			 var row2_inp4 = document.createElement("button");
             row2_inp4.id = "adapter_standalone";
			 row2_inp4.name = "Adapter"+d;

             row2_inp4.setAttribute('onclick', "openModal(this.name)");
//             row2_inp4.setAttribute('onclick', 'addModal()');
			 row2_inp4.innerHTML = "Adapter";
             row2_td4.appendChild(row2_inp4);

              var row2_inp5  = document.createElement("select");
            row2_inp5.id = "FW_upgrade_process";
            row2_inp5.name = "FW_Upgrade";
                for(i=0;i<arr_upgradeprocess.length;i++){
               var option = document.createElement("option");
               option.text = arr_upgradeprocess[i];
               option.value = arr_upgradeprocess[i];
               row2_inp5.appendChild(option);
               }
            row2_td5.appendChild(row2_inp5);

            row1_inp6 = document.createElement("button");
            row1_inp6.id = "stand_button";
            row1_inp6.innerHTML = "Submit";
            row1_inp6.name = "standalonesubmit";
         //   div_but.appendChild(row1_inp6);

          //  row1.appendChild(row1_inp6);

			row1.appendChild(row1_td1);
			row1.appendChild(row1_inp2);
			row1.appendChild(row1_td3);
			row1.appendChild(row1_td4);
			row1.appendChild(row1_td5);
			row2.appendChild(row2_inp2);
			row2.appendChild(row2_td3);
			row2.appendChild(row2_td4);
			row2.appendChild(row2_td5);
		//	row1.appendChild(row1_td6);
			div_standalone.appendChild(row1);
			div_standalone_row2.appendChild(row2);
           div_standalone.appendChild(div_standalone_row2);
           div_standalone_row2.style.display = "none";

            row1_ucsm.appendChild(row1_ucsm_td1);
            row2_ucsm.appendChild(row1_ucsm_td2);
            row2_ucsm.appendChild(row1_ucsm_td3);
            row1_ucsm.appendChild(row1_ucsm_td4);
            row1_ucsm.appendChild(row1_ucsm_td5);
            row1_ucsm.appendChild(row1_ucsm_td6);
            row1_ucsm.appendChild(row1_ucsm_td7);
            row2_ucsm.appendChild(row2_ucsm_td1);
            row2_ucsm.appendChild(row2_ucsm_td2);
            row2_ucsm.appendChild(row2_ucsm_td3);
            row2_ucsm.appendChild(row2_ucsm_td4);

            div_ucsm.appendChild(row1_ucsm);
            div_ucsm_row2.appendChild(row2_ucsm);
            div_ucsm.appendChild(div_ucsm_row2);
            div_ucsm_row2.style.display = "none";

            if((x =="Dynamic TestBed Setup")){

                if(team == "Rack OS-Compat-Standalone"){
//                alert("inside standalone");
                divid.appendChild(div_standalone);
                mdiv.appendChild(modaldiv);
            //    divid.appendChild(row1_inp6);
                document.getElementById('teamsel').style.borderColor = "black";

                }

            if(team == "Rack OS-Compat-UCSM"){
//              alert("inside UCSM");
                divid.appendChild(div_ucsm);
                mdiv.appendChild(modaldiv);
                document.getElementById('teamsel').style.borderColor = "black";

            }

            if(team =="Team"){
                alert("Please Select the team");
                document.getElementById('teamsel').style.borderColor = "red";
				 document.getElementById("testbed").selectedIndex = "0";

            }
            }
    }




    function selectfunc() {
		
        var x = document.getElementById("execsel").value;
        var testbed = document.getElementById("testselect").value;
        var newdiv = document.getElementById("maindiv");
     //   var mdiv = document.getElementById("maindiv");
     //   var divid2 = document.getElementById("testdbedsetup");
		var team = document.getElementById("teamsel").value;
		var setup = document.getElementById("testselect").value;

       // a=a+1;
       // b=a-1-b;
		
		b = b+1;
		//alert("b is"+b);
		// alert(team);
        var divid = document.getElementById("execseldiv");
//        var divid1 = document.getElementById("execseldiv");
        //var div1 = document.getElementById("sample");
        var div_fi = document.createElement("div");
		div_fi.name = "finame";
		div_fi.className = "ucsmdiv";
      //  div_fi.id = "sample";
        var activitylabel = document.createElement("input");
			activitylabel.value = team +"-" +b;
			activitylabel.name = "actlabel";
			activitylabel.className = "actlabel";
			activitylabel.readOnly = "true";
			div_fi.appendChild(activitylabel);

        var arr_server = ['Server','C460-M4','C22-M3','C24-M3','C220-M3','C240-M3','C220-M4','C240-M4','C3X60-M3','C3X60-M4','C480-M5'];
        var arr_serverboottype = ['Boot Type','LEGACY','UEFI'];
        var arr_adapter = ['Adapter','9361','Bcm5709'];
        var arr_osbootmode = ['Boot Method','PXE','V-ISO','DVD-ROM'];
        var arr_slot = ['Slot','1','2','HBA'];
        var arr_boot = ['Boot','SAN','ISCSI','LOCAL'];
//        var arr_os = ['OS','Rhel6.7','Rhel 6.8'];
        var arr_result = ['Pass','Fail'];
        var arr_auto = ['Automation','CAS','IAS','No'];


      var div_standalone = document.createElement("div");
             div_standalone.id = "standalone_div_id";
             div_standalone.className = "standalone"+b;
			 div_standalone.name = "server_div";


	  var activitylabel = document.createElement("input");
			activitylabel.value = setup + '-' + document.getElementById('execsel').value;
			activitylabel.name = "actlabel";
			activitylabel.id = "actlabel"+b;
			activitylabel.className = "actlabel";
			activitylabel.readOnly = "true";
			div_standalone.appendChild(activitylabel);
           var servertable = document.createElement("table");
           servertable.id = "fitab1";

          var row2 = document.createElement("tr");
          row2.id = "row2_execution";

           var row3 = document.createElement("tr");
            row3.id = "row3_execution";

//          var row2_td1 = document.createElement("td");
//          var row2_td2 = document.createElement("td");
//          row2_td2.id = "firstinp";
          var row2_td3 = document.createElement("td");
           row2_td3.id = "pxeadap";
           var row2_td4 = document.createElement("td");
           row2_td4.id = "drivversion";
           var row2_td5 = document.createElement("td");
           var row2_td6 = document.createElement("td");

          var row2_inp5 = document.createElement("select");
            row2_inp5.id = "osbootmethod";
			row2_inp5.name = "Boot_Type"+b;
            row2_inp5.setAttribute('onchange', 'enablepxeadapter(this.name)');

			row2_inp5.className = "Boot_type_class";
               for(i=0;i<arr_osbootmode.length;i++){
               var option = document.createElement("option");
               option.text = arr_osbootmode[i];
               option.value = arr_osbootmode[i];
               row2_inp5.appendChild(option);
           }
           var row2_inp2  = document.createElement("select");
            row2_inp2.id = "osname";
            row2_inp2.name = "os_name"+b;
            row2_inp2.className = "os_name";

                for(i=0;i<arr_os.length;i++){
               var option = document.createElement("option");
               option.text = arr_os[i];
               option.value = arr_os[i];
               row2_inp2.appendChild(option);
           }

          var row2_inp3  = document.createElement("input");
			row2_inp3.placeholder = " Enter Pxe Adapter";
			row2_inp3.name = "Pxe_adapter"+b;
			 row2_inp3.id = "pxe_adapter"+b;
			 row2_inp3.style.height = "40px";
			 row2_inp3.style.width = "180px";
			 row2_inp3.style.background = "#eee";
			 row2_inp3.style.border = "1px groove";
			 row2_inp3.disabled = "true";

			 row2_inp3.className = "pxeadapinp";
			 row2_inp3.style.backgroundColor = "#d9d9d9";
//			 row2_td2.appendChild(row2_inp2);
			 row2_td3.appendChild(row2_inp3);

			var row2_inp4  = document.createElement("button");
			row2_inp4.innerHTML = "Driver Version";
			row2_inp4.name = "Driver_version"+b;
		  //row2_inp4.id = "driver_btn";
			row2_inp4.className = "Driver_version";
//			var tb = document.getElementById('actlabel').value;
			row2_inp4.setAttribute('onclick', 'adddriver(this.name)');
			row2_td4.appendChild(row2_inp4);
            row2_inp4.id = "driverversion";

            var row2_inp6 = document.createElement("select");
            row2_inp6.id = "serverboottype";
			row2_inp6.name = "server_boottype"+b;
               for(i=0;i<arr_serverboottype.length;i++){
               var option = document.createElement("option");
               option.text = arr_serverboottype[i];
               option.value = arr_serverboottype[i];
               row2_inp6.appendChild(option);
           }
           row2_td6.appendChild(row2_inp6);

//            row2.appendChild(row2_inp1);

//            row2.appendChild(row2_td3);
            row2.appendChild(row2_inp2);
            row2.appendChild(row2_td4);
            row2.appendChild(row2_inp5);
            row2.appendChild(row2_td3);
            row2.appendChild(row2_td6);
            servertable.appendChild(row2);
            //div_server.appendChild(row2);
            div_standalone.appendChild(row2);
            div_standalone.appendChild(row3);


          var ostable = document.createElement("table");
          ostable.id = "fitab";
          var row4 = document.createElement("tr");

          var row4_td4 = document.createElement("td");
         row4_td4.id = "firstinp";
//          var row4_td5 = document.createElement("td");

          var row4_td6 = document.createElement("td");
          row4_td6.id = "cdets";
          var row4_td7 = document.createElement("td");
          row4_td7.id = "comments";
          var row4_td9 = document.createElement("td");
          row4_td9.id = "Efforts";

           var row4_td8 = document.createElement("td");

            var row4_inp1 = document.createElement("select");
            row4_inp1.id = "automation_select";
            row4_inp1.className = "auto_sel"
			row4_inp1.name = "auto_type"+b;
				row4_inp1.setAttribute('onchange', 'enablelinklog(this.name)');
               for(i=0;i<arr_auto.length;i++){
               var option = document.createElement("option");
               option.text = arr_auto[i];
               option.value = arr_auto[i];
               row4_inp1.appendChild(option);
           }
//            var row4_inp2 =  document.createElement("select");
//            row4_inp2.id = "fidetailsel";
//            row4_inp2.name = "osbootmode";
//                  for(i=0;i<arr_osbootmode.length;i++){
//               var option = document.createElement("option");
//               option.text = arr_osbootmode[i];
//               option.value = arr_osbootmode[i];
//               row4_inp2.appendChild(option);
//           }
		    var row4_inp4  = document.createElement("input");
			row4_inp4.placeholder = "Link for Logs";
			row4_inp4.name = "Link_Automation"+b;
			row4_inp4.disabled = "true";
			row4_inp4.className = "Link_Logs";
			row4_inp4.style.backgroundColor = "#d9d9d9";
			row4_inp4.id = "linklog"+b;
			row4_inp4.style.height = "40px";
			 row4_inp4.style.width = "180px";
//			 row4_inp4.style.background = "#eee";
			 row4_inp4.style.border = "1px groove";
			 row4_inp4.disabled = "true";
			 row4_inp4.style.backgroundColor = "#d9d9d9";
			row4_td4.appendChild(row4_inp4);

           var row4_inp8 = document.createElement("select");
            row4_inp8.id = "result";
			row4_inp8.name = "Result"+b;
               for(i=0;i<arr_result.length;i++){
               var option = document.createElement("option");
               option.text = arr_result[i];
               option.value = arr_result[i];
               row4_inp8.appendChild(option);

           }
		   row4_td8.appendChild(row4_inp8);

		    var row4_inp6  = document.createElement("input");
			row4_inp6.placeholder = "CDETS Link";
			row4_inp6.id ="cdetlink";
			row4_inp6.name = "LinkForLogs"+b;
			row4_td6.appendChild(row4_inp6);

			var row4_inp7  = document.createElement("input");
			row4_inp7.placeholder = "Comments";
			row4_inp7.name = "Remarks"+b;
			row4_inp7.id = "comment";
			row4_td7.appendChild(row4_inp7);

            var row4_inp9 = document.createElement("input");
            row4_inp9.type = "number";
            row4_inp9.placeholder = "Effort in HRS";
            row4_inp9.id = "Effort_Spent";
            row4_inp9.name = "Effortspent"+b;
            row4_inp9.style.width = "120px";
			row4_inp9.setAttribute('required','required');
            row4_td9.appendChild(row4_inp9);

            row4.appendChild(row4_inp1);
         //   row4.appendChild(row4_td2);

            row4.appendChild(row4_td4);
//            row4.appendChild(row4_inp2);
         //   row4.appendChild(row4_inp5);
            row4.appendChild(row4_td6);
            row4.appendChild(row4_td7);
            row4.appendChild(row4_td8);
            row4.appendChild(row4_td9);




             ostable.appendChild(row4);
            div_standalone.appendChild(row4);


        if ((testbed != "Choose Test Bed Setup")&&(x != "Select Release")) {
                divid.appendChild(div_standalone);
                 document.getElementById('teamsel').style.borderColor = "black";
				  document.getElementById("testselect").selectedIndex = "0";
		}
		if(x =="Select Release"){
			alert("please select proper release");
			 document.getElementById("testselect").selectedIndex = "0";
			document.getElementById('execsel').style.borderColor = "red";
		}
		if(x !="Select Release"){
			
			document.getElementById('execsel').style.borderColor = "black";
		}
		
        return false;
    }



function checkInput(){


//    var a  = document.getElementById("testbedsetup").innerHTML;
    var b = document.getElementsByClassName("execution")[0].innerHTML;

//    alert("a is"+b);
    if(b == "Execution"){
        var x = document.getElementById("testdbedsetup");
            x.style.display = "none";
          var troubleshoot = document.getElementById("testedselect_troubleshoot");
        troubleshoot.style.display = "none";
    }

}

function checktestbed(){
//    alert("insid testbed");
    var a  = document.getElementsByClassName("testbedsetup")[0].innerHTML;
//    alert("a is"+a);
    if(a=="TestBed Setup"){
     var y = document.getElementById("execseldiv");
    y.style.display = "none";
     var z=  document.getElementById("testedselect");
         z.style.display = "none";
     var troubleshoot = document.getElementById("testedselect_troubleshoot");
        troubleshoot.style.display = "none";

    }

}

function checktroubleshoot(){

    var troubleshoot = document.getElementsByClassName("Troubleshoot")[0].innerHTML;

       if(troubleshoot == "Troubleshoot"){
          var y = document.getElementById("testdbedsetup");
           y.style.display = "none";
             var z = document.getElementById("execseldiv");
             z.style.display = "none";
             var x = document.getElementById("testedselect");
             x.style.display = "none";

       }

}

function display_re(){

    var troubleshoot = document.getElementsByClassName("fwselect")[0].innerHTML;
        //alert(troubleshoot);
       if(troubleshoot == "Firmware Review"){
       //alert("inside if.......");
          var y = document.getElementById("fwReview");
           y.style.display = "none";
             var z = document.getElementById("sub1");
             z.style.display = "none";
             var x = document.getElementById("fwreview");
             x.style.display = "none";

       }

}

function enablepxeadapter(name){
	tmp_name = name;
	var res = tmp_name.split(/\D/);
	//alert("res is"+res[9]);
    var adap  = document.getElementsByClassName("Boot_type_class")[0].value;
    var auto = document.getElementsByClassName("auto_sel")[0].value;
  //  for(var i=0;i<=b;i++){

          var na =  document.getElementsByName("Boot_Type"+res[9])[0].value;

    if(na == "PXE"){
	//	alert("na is"+na);
         document.getElementById("pxe_adapter"+res[9]).disabled = false;
        document.getElementById("pxe_adapter"+res[9]).style.backgroundColor = "#eee";

    }

    else {
        document.getElementById("pxe_adapter"+res[9]).value = "";
        document.getElementById("pxe_adapter"+res[9]).disabled = true;
        document.getElementById("pxe_adapter"+res[9]).style.backgroundColor = "#d9d9d9";

    }
 //   }
}
 function enablelinklog(name){
		tmp_name = name;
		var res = tmp_name.split(/\D/);
	//	alert("res is"+res[9]);
         var na =  document.getElementsByName("auto_type"+res[9])[0].value;
    if((na =="CAS")||(na =="IAS")){
        //linklog auto_type
        document.getElementById("linklog"+res[9]).disabled = false;
        document.getElementById("linklog"+res[9]).style.backgroundColor = "#eee";

    }
    else{
            document.getElementById("linklog"+res[9]).value = "";
             document.getElementById("linklog"+res[9]).disabled = true;
             document.getElementById("linklog"+res[9]).style.backgroundColor = "#d9d9d9";

    }
    }
 function deleteModal(id){

	 tmp_id = id;
		var res = tmp_id.split(/\D/);
	 var clas = document.getElementById("Standalone_modal").className;
	 alert("clas is"+res[3]);

	 var s = document.getElementById("selid"+res[3]);
	 
		s.removeChild(document.getElementsByClassName("st_mod"+res[3]));
		s.removeChild(document.getElementsByClassName("st_mod"+res[3]));
	//	document.getElementsByClassName("st_mod"+res[3]).removeChild;
	 
 }

/*$(document).ready(function(){
    $(".del").click(function(){
        $("#box").remove();
    });
}); */
//} 
