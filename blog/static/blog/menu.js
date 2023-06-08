var sel_ = null; //menu duoc chon

function MO(r) {
  if (r != sel_) r.className = "menu-move";
}

function MOut(r) {
  if (r != sel_) r.className = "menu-normal";
}

function MC(r) {
  if (sel_ != null)
    //thuc don hien tai duoc chon
    sel_.className = "menu-normal";

  sel_ = r; //thuc don moi duoc chon
  sel_.className = "menu-select";

  //thuc hien cac viec khi noi dung nay duoc chon
  //document.getElementById("alo").innerHTML = sel_.innerHTML;

  var frm = document.getElementById("myframe");
  if (sel_.id == "m1") {
    frm.src = "https://vnexpress.net";
  } else if (sel_.id == "m2") {
    frm.src = "https://dantri.com.vn";
  } else if (sel_.id == "m3") {
    frm.src = "https://vtv.vn/";
  } else if (sel_.id == "m4") {
    frm.src = "https://zingnews.vn/";
  }
}
