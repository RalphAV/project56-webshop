//A jquery function to combine the filter and orderby forms

function combineForms() {
    //SEE IF THIS CAN BE REWRITTEN INTO 1 SELECTOR FOR BOTH FORMS
    var $newForm = $("<form></form>")
        .attr({method: "GET", action : ""});

    $('form[name="filterform"] :text, :checked').each(function () {
        $newForm.append($("<input type=\"hidden\" />")
            .attr('name', this.name)
            .val($(this).val())
        );
    });
    $('form[name="orderform"] :input:not(:submit, :button)').each(function () {
        $newForm.append($("<input type=\"hidden\" />")
            .attr('name', this.name)
            .val($(this).val())
        );
    });

    $newForm
        .appendTo(document.body)
        .submit();
    }