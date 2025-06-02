function toggleIframe(iframe_id) {
    if (document.getElementById(iframe_id).style.display == "block") {
        document.getElementById(iframe_id).style.display = "none";
        return true;
    }
    else { document.getElementById(iframe_id).style.display = "block"; return false;};
}