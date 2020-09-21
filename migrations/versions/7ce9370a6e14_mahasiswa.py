"""mahasiswa

Revision ID: 7ce9370a6e14
Revises: 
Create Date: 2020-09-21 09:54:59.206923

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7ce9370a6e14'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=230), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=128), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_table('mahasiswas',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('nim', sa.String(length=10), nullable=False),
    sa.Column('nama_mahasiswa', sa.String(length=100), nullable=False),
    sa.Column('mutu', sa.Integer(), nullable=False),
    sa.Column('jumlah_sks', sa.Integer(), nullable=False),
    sa.Column('ipk', sa.Float(precision=2, asdecimal=2), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.BigInteger(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('nim')
    )
    op.create_index(op.f('ix_mahasiswas_created_at'), 'mahasiswas', ['created_at'], unique=False)
    op.create_index(op.f('ix_mahasiswas_updated_at'), 'mahasiswas', ['updated_at'], unique=False)
    op.create_table('todos',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('todo', sa.String(length=140), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.BigInteger(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_todos_created_at'), 'todos', ['created_at'], unique=False)
    op.create_index(op.f('ix_todos_updated_at'), 'todos', ['updated_at'], unique=False)
    op.create_table('todo_files',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('file_name', sa.Text(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('todo_id', sa.BigInteger(), nullable=True),
    sa.ForeignKeyConstraint(['todo_id'], ['todos.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_todo_files_created_at'), 'todo_files', ['created_at'], unique=False)
    op.create_index(op.f('ix_todo_files_updated_at'), 'todo_files', ['updated_at'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_todo_files_updated_at'), table_name='todo_files')
    op.drop_index(op.f('ix_todo_files_created_at'), table_name='todo_files')
    op.drop_table('todo_files')
    op.drop_index(op.f('ix_todos_updated_at'), table_name='todos')
    op.drop_index(op.f('ix_todos_created_at'), table_name='todos')
    op.drop_table('todos')
    op.drop_index(op.f('ix_mahasiswas_updated_at'), table_name='mahasiswas')
    op.drop_index(op.f('ix_mahasiswas_created_at'), table_name='mahasiswas')
    op.drop_table('mahasiswas')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###
