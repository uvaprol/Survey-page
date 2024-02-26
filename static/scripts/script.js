function sendOffer() {
    let orgName         = $("#orgName").val();
    let shortOrgName    = $("#shortOrgName").val();
    let userType        = $("#userType").val();
    let bossPost        = $("#bossPost").val();
    let bossName        = $("#bossName").val();
    let responsiblePost = $("#responsiblePost").val();
    let responsibleName = $("#responsibleName").val();
    let tel             = $("#tel").val();
    let mail            = $("#e-mail").val();
    $.get("/sendOffer", {
        'orgName'         : orgName,
        'shortOrgName'    : shortOrgName,
        'userType'        : userType,
        'bossPost'        : bossPost,
        'bossName'        : bossName,
        'responsiblePost' : responsiblePost,
        'responsibleName' : responsibleName,
        'tel'             : tel,
        'mail'            : mail
    });
    $("#orgName").val('')
    $("#shortOrgName").val('')
    $("#userType").val('')
    $("#bossPost").val('')
    $("#bossName").val('')
    $("#responsiblePost").val('')
    $("#responsibleName").val('')
    $("#tel").val('')
    $("#e-mail").val('')
}

