shear = True
punch = True
form = True
bend = True
buffer = [0, 0, 0]
buffer_size = 1
processed = 0
die_change = [500, 400, 750, 600]
simulation = 100
t = 0
shear_cnt = 0
shear_rst = 0
punch_cnt = 0
punch_rst = 0
form_cnt = 0
form_rst = 0
bend_cnt = 0
bend_rst = 0

while t < simulation:
    t += 1
    if shear:
        buffer[0] += min(4.5, buffer_size)
        shear_cnt += buffer[0]

    if shear_cnt >= die_change[0]:
        shear = False
        shear_rst = 25
    shear_rst -= 1

    if shear == False and shear_rst == 0:
        shear = True

    if punch and buffer[0] > 0:
        buffer[1] += min(5.5, buffer[0])
        buffer[0] = max(0, buffer[0] - buffer[1])
        punch_cnt += buffer[1]

    if punch_cnt >= die_change[1]:
        punch = False
        punch_rst = 25
    punch_rst -= 1

    if shear == False and punch_rst == 0:
        punch = True

    if form and buffer[1] > 0:
        buffer[2] += min(3.8, buffer[1])
        buffer[1] = max(0, buffer[1] - buffer[2])

        form_cnt += buffer[2]

    if form_cnt >= die_change[2]:
        form = False
        form_rst = 25
    form_rst -= 1

    if form == False and form_rst == 0:
        form = True

    if bend and buffer[2] > 0:
        processed += min(3.2, buffer[2])
        buffer[2] = max(0, buffer[2] - processed)
        bend_cnt += processed

    if bend_cnt >= die_change[3]:
        bend = False
        bend_rst = 25

    bend_rst -= 1

    if bend == False and bend_rst <= 0:
        bend = True
print(processed)