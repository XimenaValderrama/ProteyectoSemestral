function msj(){
    const swalWithBootstrapButtons = Swal.mixin({
        customClass: {
          confirmButton: 'btn btn-success',
          cancelButton: 'btn btn-danger'
        },
        buttonsStyling: false
      })
      
      swalWithBootstrapButtons.fire({
        title: 'Estas seguro de continuar?',
        text: "Podrás volver a suscribirte!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonText: 'Sí',
        cancelButtonText: 'No',
        reverseButtons: true
      }).then((result) => {
        if (result.isConfirmed) {
          swalWithBootstrapButtons.fire(
            'Suscripción cancelada!',
          )
        } else if (
          /* Read more about handling dismissals below */
          result.dismiss === Swal.DismissReason.cancel
        ) {
          swalWithBootstrapButtons.fire(
            'Tu suscripción se mantendrá :)',
          )
        }
      })
}

function carro(){
  Swal.fire({
    icon: 'success',
    title: 'Producto Añadido',
  })
}

function off(){
  const swalWithBootstrapButtons = Swal.mixin({
      customClass: {
        confirmButton: 'btn btn-success',
        cancelButton: 'btn btn-danger'
      },
      buttonsStyling: false
    })
    
    swalWithBootstrapButtons.fire({
      title: 'Cerrar Sesión?',
      icon: 'question',
      showCancelButton: true,
      confirmButtonText: 'Sí',
      cancelButtonText: 'No',
      reverseButtons: true
    }).then((result) => {
      if (result.isConfirmed) {
        swalWithBootstrapButtons.fire(
          'Sesión Cerrada!',
        )
      } else if (
        /* Read more about handling dismissals below */
        result.dismiss === Swal.DismissReason.cancel
      ) {
        swalWithBootstrapButtons.fire(
          'Sigue disfrutando',
        )
      }
    })
}

function Eliminar(codigo){
  Swal.fire({
    title: 'Esta seguro?',
    text: "Se eliminará permanentemente!",
    icon: 'question',
    showCancelButton: true,
    confirmButtonColor: '#3085d6',
    cancelButtonColor: '#d33',
    confirmButtonText: 'Sí, eliminar!',
    cancelButtonText: 'Cancelar'
  }).then((result) => {
    if (result.isConfirmed) {
      Swal.fire({
          title: "Eliminado!",
          text: "Producto eliminado",
          icon: 'success'
      }).then (function(){
        window.location.href = "/eliminarProducto/" + codigo + "/";
      })
    }
  })
}

function EliminarUsuario(rut){
  Swal.fire({
    title: 'Esta seguro?',
    text: "Se eliminará permanentemente!",
    icon: 'success',
    showCancelButton: true,
    confirmButtonColor: '#3085d6',
    cancelButtonColor: '#d33',
    confirmButtonText: 'Sí, eliminar!',
    cancelButtonText: 'Cancelar'
  }).then((result) => {
    if (result.isConfirmed) {
      Swal.fire({
          title: "Eliminado!",
          text: "Usuario eliminado",
          icon: 'success'
      }).then (function(){
        window.location.href = "/eliminarUsuario/" + rut + "/";
      })
    }
  })
}
function EliminarCarrito(id_producto){
  Swal.fire({
    title: '¿Esta seguro?',
    text: "Se eliminará del carrito!",
    icon: 'question',
    showCancelButton: true,
    confirmButtonColor: '#3085d6',
    cancelButtonColor: '#d33',
    confirmButtonText: 'Sí, eliminar!',
    cancelButtonText: 'Cancelar'
  }).then((result) => {
    if (result.isConfirmed) {
      Swal.fire({
          title: "Eliminado!",
          text: "Producto eliminado",
          icon: 'success'
      }).then (function(){
        window.location.href = "/EliminarDeCarrito/" + id_producto + "/";
      })
    }
  })
}


function PagarCarrito(){
  Swal.fire({
    title: 'Pago realizado',
    text: "Su pago ha sido efectuado correctamente",
    icon: 'success',
    type: 'success',
    confirmButtonColor: '#3085d6',
    confirmButtonText: 'OK',
  }).then(function(){
        window.location.href = "/ResetCarrito/";
      });
}



