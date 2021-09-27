#Alwin Wezenbeek 99060433

vraag_geel = input('is de kaas geel? ')

if vraag_geel == 'y' or vraag_geel == 'Y':
    vraag_gaten = (input('zitten er gaten in? '))
    if vraag_gaten == 'y' or vraag_gaten == 'Y':
        vraag_duur = (input('is de kaas belachelijk duur? '))
        if vraag_duur == 'y' or vraag_duur == 'Y':
            print('Emmenthaler')
        else:
            print('Leerdammer')
    else:
        vraag_hard = (input('is de kaas hard als steen? '))
        if vraag_hard == 'y' or vraag_hard == 'Y':
            print('Pammigiano Reggiano')
        else:
            print('Goudse kaas')

else:
    vraag_schimmels = (input('heeft de kaas blauwe schimmels? '))
    if vraag_schimmels == 'y' or vraag_schimmels == 'Y':
        vraag_korst = (input('heeft de kaas een korst? '))
        if vraag_korst == 'y' or vraag_korst == 'Y':
            print('Blue de Rochbaron')
        else:
            print('''foumme d'ambert''')
    else:
        vraag_korst2 = (input('heeft de kaas een korst? '))
        if vraag_korst2 == 'y' or vraag_korst2 == 'Y':
            print('Camembert')
        else:
            print('Mozzarella')



