n_rows = 128
n_cols = 8

fb_chars = (0, 7)
lr_chars = (8,10)

def read_file(filename):
    with open(filename) as f:
        content = [x.strip() for x in f]
        return content

def get_seat(ticket):
    row_part = ticket[0:7]
    col_part = ticket[7::]

    max = n_cols
    min = 0

    for c in col_part:
        if (c == 'R'):
           min = (min+max)/2
        elif (c == 'L'):
           max = (min+max)/2

    col = (max+min)/2

    max = n_rows
    min = 0
    for c in row_part:
        if (c == 'B'):
            min = (min+max)/2
        elif (c == 'F'):
            max = (min+max)/2

    row = (max+min)/2

    return (row, col)

def to_id(row, col):
    return row*8 + col

def main(filename):

    tickets = read_file(filename)
    ids = []

    for ticket in tickets:
        r, c = get_seat(ticket)
        ids.append(to_id(r,c))
    
    return max(ids)

if __name__ == "__main__":
    print(main("input-5.txt"))
    

    #print('BFFFBBFRRR: row 70, column 7, seat ID 567 ',  get_seat("BFFFBBFRRR"))
    #print('FFFBBBFRRR: row 14, column 7, seat ID 119 ',  get_seat("FFFBBBFRRR"))
    #print('BBFFBBFRLL: row 102, column 4, seat ID 820',  get_seat("BBFFBBFRLL"))



            
        

