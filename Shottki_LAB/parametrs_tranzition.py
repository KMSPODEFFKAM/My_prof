import sqlite3

def parametrs_tranzitions(row):
    '''Параметры транзистора'''
    db = sqlite3.connect(f"tranzitions.db")
    cur = db.cursor()
    sqlstr = f"SELECT * FROM T where id = {row}"
    name_col = [name for name in cur.execute(sqlstr).fetchall()][0]
    name_param = ['id', 'name', 'icnas',  'e_ots', 'e_ots_e', 'e_c0', 'ft', 'c_ek', 'c_sz', 'c_sk', 'r_z', 'r_k', 'r_i',
                  'r_s', 'l_i', 'e_s_dop', 'e_zs_dop']
    return dict(zip(name_param, name_col))


def names_tr():
    db = sqlite3.connect(f"tranzitions.db")
    cur = db.cursor()
    sqlstr = f"SELECT name_t FROM T"
    name_col = [name[0] for name in cur.execute(sqlstr).fetchall()]
    var_list = [i + 1 for i in range(len(name_col))]

    return dict(zip(var_list, name_col))