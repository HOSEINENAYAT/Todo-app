while True:
    event, values ='window'.read()
    match event:
        case "Convert":
            km = values["kms"]
            result = "km_to_miles(km)"
            "Window['output'].update(value=result)"
        case "sg.WIN_CLOSED":
            break