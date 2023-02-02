# pylint: disable=invalid-name
"""Add providence to auditmathtype

Revision ID: 754cca3f4448
Revises: 6a4dc1ef268c
Create Date: 2023-02-02 15:54:54.693933+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "754cca3f4448"
down_revision = "6a4dc1ef268c"
branch_labels = None
depends_on = None

# source: https://stackoverflow.com/questions/14845203/altering-an-enum-field-using-alembic
old_options = ("BRAVO", "MINERVA", "SUPERSIMPLE", "MACRO", "SUITE")
new_options = sorted(old_options + ("PROVIDENCE",))

old_type = sa.Enum(*old_options, name="auditmathtype")
new_type = sa.Enum(*new_options, name="auditmathtype")
tmp_type = sa.Enum(*new_options, name="_auditmathtype")


def upgrade():
    # Create a temporary "_audit_math_type" type, convert and drop the "old" type
    tmp_type.create(op.get_bind(), checkfirst=False)
    op.execute(
        "ALTER TABLE election ALTER COLUMN audit_math_type TYPE _auditmathtype"
        " USING audit_math_type::text::_auditmathtype"
    )
    old_type.drop(op.get_bind(), checkfirst=False)
    # Create and convert to the "new" audit_math_type type
    new_type.create(op.get_bind(), checkfirst=False)
    op.execute(
        "ALTER TABLE election ALTER COLUMN audit_math_type TYPE auditmathtype"
        " USING audit_math_type::text::auditmathtype"
    )
    tmp_type.drop(op.get_bind(), checkfirst=False)


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
