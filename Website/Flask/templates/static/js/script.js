$(document).ready(function(){
    $("#Start").click(function(){
        $("#main").html("<iframe src=\"./info.php\"></iframe>");
        $("iframe").focus();
    });
});
