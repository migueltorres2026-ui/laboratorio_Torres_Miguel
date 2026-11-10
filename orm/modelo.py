from sqlalchemy import Integer, String, Date, CheckConstraint, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class Equipo(Base):
    __tablename__ = "Equipo"
    __table_args__ = (
        CheckConstraint("stock_disponible >= 0",name="CK_stock_Equipo" ,),
    )

    id: Mapped[int] = mapped_column( Integer, primary_key=True)
    nombre: Mapped[str] = mapped_column( String, nullable=False)
    tipo: Mapped[str] = mapped_column( String, nullable=False)
    stock_disponible: Mapped[int] = mapped_column( Integer, nullable=False, default=0)

    def __repr__(self):
        (
        f"Epuipo(id={self.id})",
        f"nombre={self.nombre!r}",
        f"tipo={self.tipo}",
        f"stock_disponible={self.stock_disponible}"
        )

class Estudiante(Base):
    __tablename__ = "Equipo"

    id: Mapped[int] = mapped_column( Integer, primary_key=True)
    nombre: Mapped[str] = mapped_column( String, nullable=False)
    correo: Mapped[str] = mapped_column( String, nullable=False)

    def __repr__(self):
        (
        f"Estudiante(id={self.id})",
        f"nombre={self.nombre!r}",
        f"correo={self.correo!r}"
        )

class Prestamo(Base):
    __tablename__ = "prestamo"
    __table_args__ = (
        CheckConstraint("cantidad > 0",name="CK_cantidad_prestamo",),
    )
    
    id: Mapped[int] = mapped_column( Integer, primary_key=True)
    equipo_id: Mapped[int] = mapped_column( Integer, ForeignKey("equipo.id"))
    Estudiante_id: Mapped[int] = mapped_column( Integer, ForeignKey("estudiante.id"))
    fecha: Mapped[Date] = mapped_column( Date, nullable=False)
    cantidad: Mapped[int] = mapped_column( Integer, nullable=False)


    def __repr__(self):
        (
        f"Prestamo(id={self.id})",
        f"equipo_id={self.equipo_id}",
        f"estudiante_id={self.Estudiante_id}",
        f"fecha={self.fecha}",
        f"cantidad={self.cantidad}"
        )

