<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://code.jquery.com/jquery-3.4.1.min.js"></script>
    <script src="{{url_for('static', filename='js/snake.js')}}"></script>
    <title></title>
</head>
<body>
    <input type="hidden" id="Snake_length">
    <input type="hidden" id="Init_x">
    <input type="hidden" id="Init_y">
    <input type="hidden" id="Direction">
    <div id="Game">
        <table id="Canvas" border="5px red solid" RULES="none">
            <?for($i = 0; $i < 75; $i++){?>
            <tr id=<?echo $i;?>>
                <?for($j = 0; $j < 170; $j++){?>
                <td style="width:10px; height:10px; background-color:black;" id=<?echo "$i-$j";?>></td>
                <?}?>
            </tr>
            <?}?>
        </table>
    </div>
</body>
</html>