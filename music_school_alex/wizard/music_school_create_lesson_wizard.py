from odoo import models, fields, api
from datetime import timedelta

'''
Permite a los usuarios seleccionar un curso y especificar un rango de fechas para crear lecciones diarias.
Clases:
- MusicSchoolCreateLesson: Asistente para crear lecciones a partir de un curso y un rango de fechas.
Campos:
- course_id: Relación con el curso para el cual se están creando las lecciones.
- start_date: Fecha y hora de inicio de las lecciones.
- end_date: Fecha y hora de finalización de las lecciones.
Métodos:
- action_create_lessons: Crea lecciones diarias desde la fecha de inicio hasta la fecha de finalización,
  asignando cada lección al curso seleccionado.
'''

class MusicSchoolCreateLesson(models.TransientModel):
    _name = 'music.school.create.lesson'
    _description = 'This wizard allows you to create injuries from the calendar'

    course_id = fields.Many2one(
        comodel_name='music.school.course',
        string="Course",
        required=True,
        help="Course for which the lessons are created"
    )
    start_date = fields.Datetime(
        string="Start Date",
        required=True,
        help="Start date of lessons"
    )
    end_date = fields.Datetime(
        string="End Date",
        required=True,
        help="End date of lessons"
    )

    def action_create_lessons(self):
        import pdb;pdb.set_trace()
        lesson_obj = self.env['music.school.lesson']
        current_date = self.start_date
        lesson = self.env['music.school.lesson']
        while current_date <= self.end_date:
            lesson |= lesson_obj.create({
                'course_id': self.course_id.id,
                'date': current_date,
            })
            current_date += timedelta(days=1)
        return {
            'type': 'ir.actions.act_window',
            'name': 'Lessons',
            'res_model': 'music.school.lesson',
            'view_mode': 'list,form',
            'domain': [('id', 'in', lesson.ids)],
            'target': 'current',
        }