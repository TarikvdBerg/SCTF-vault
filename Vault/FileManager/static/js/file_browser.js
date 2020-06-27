var currentlySelected = null

function GetFolderContents(fid, sucFunc, failFunc) {
    $.ajax({
        type: "GET",
        url: "/files/file_browser/get_folder_content/",
        data: {
            fid: fid,
        },
        success: sucFunc,
        error: failFunc,
    })
}

function SetBreadCrumb(path) {
    $("#filepath p").text(path)
}

function PopulateFileBrowser(data) {
    data = JSON.parse(data)

    SetBreadCrumb(data.path)

    $("#browser table tr:not(:first-child)").remove();

    if (data.parent_folder != null) {
        $("#browser table").append(`
        <tr data-id="${data.parent_folder}" onclick="RowClick('${data.parent_folder}')">
            <td>${FOLDER_ICON}</td>
            <td>..</td>
            <td></td>
            <td>Folder</td>
            <td></td>
            <td></td>
        </tr>
        `)
    }



    data.contained_folders.forEach(function (item, index) {
        $("#browser table").append(`
        <tr data-id="${item.pk}" onclick="RowClick('${item.pk}')">
            <td>${FOLDER_ICON}</td>
            <td>${item.fields.name}</td>
            <td>${item.fields.edited}</td>
            <td>Folder</td>
            <td>${item.fields.size}</td>
            <td>${item.fields.owner}</td>
        </tr>
        `)
    })

    data.contained_files.forEach(function (item, index) {
        $("#browser table").append(`
        <tr data-id="${item.id}">
            <td>${FILE_ICON}</td>
            <td>${item.fields.name}</td>
            <td>${item.fields.edited}</td>
            <td>File</td>
            <td>${item.fields.size}</td>
            <td>${item.fields.owner}</td>
        </tr>
        `)
    })
}


function UpdateFileBrowser(fid) {
    GetFolderContents(
        fid,
        PopulateFileBrowser,
        function () {}
    )

    CURRENT_FOLDER = fid;
}

function RowClick(id) {
    if (currentlySelected != id) {
        if (currentlySelected != null) {
            $(`tr[data-id="${currentlySelected}"]`).removeClass()
        }
        currentlySelected = id;
        $(`tr[data-id="${id}"]`).addClass("selected")
        return;
    } else {
        UpdateFileBrowser(id)
    }
}

function CreateNewFolder(name_input_id) {
    folder_name = $(name_input_id).val()
    csrf_token = $('input[name="csrfmiddlewaretoken"]').val()

    if (folder_name == "") {
        return
    }
    

    $.ajax({
        method: "POST",
        url: "/files/folder/",
        data: {
            "folder_name": folder_name,
            "parent_folder": CURRENT_FOLDER,
            "csrfmiddlewaretoken": csrf_token
        },
        success: function (data) {
            UpdateFileBrowser(CURRENT_FOLDER)
            $("#close_modal").click();
            $("#folder_name").val("")
        },
        error: function(xhr) {
            alert('Failed to create folder')
        }
    })
}

function DeleteCurrentlySelectedFolder() {
    csrf_token = $('input[name="csrfmiddlewaretoken"]').val()

    $.ajax({
        method: "DELETE",
        url: `/files/folder/${currentlySelected}/`,
        beforeSend: function(xhr) {
            xhr.setRequestHeader("X-CSRFToken", csrf_token);
        },
        success: function () {
            UpdateFileBrowser(CURRENT_FOLDER)
        },
        error: function() {
            alert("Failed to delete folder")
        }
    })
}