# from docxtpl import DocxTemplate
# doc = DocxTemplate("Заявление на социальное питание обучающихся.png.doc")
# context = { 'emitent' : 'ООО Ромашка', 'address1' : 'г. Москва, ул. Долгоруковская, д. 0', 'участник': 'ООО Участник', 'адрес_участника': 'г. Москва, ул. Полевая, д. 0', 'director': 'И.И. Иванов'}
# doc.render(context)
# doc.save("шаблон.docx")
from docxtpl import DocxTemplate
from docx import Document


# doc = DocxTemplate("Заявление на социальное питание обучающихся.png.doc")
# context = { 'director' : "И.И.Иванов"}
# doc.render(context)
def docu():
    name = "Высшая школа"
    passport = "1234"
    doc = DocxTemplate("test.docx")
    context = { 'name' : name, 'nomer' : passport}
    doc.render(context)
    # document = Document('test.docx')
    # document.save('example.docx')
    doc.save("examp5.docx")
if __name__ == '__main__':
    docu()