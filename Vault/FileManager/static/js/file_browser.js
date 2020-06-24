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

    console.log(data)

    SetBreadCrumb(data.path)

    $("#browser table tr:not(:first-child)").remove();

    if (data.parent_folder != null) {
        $("#browser table").append(`
        <tr data-id="${data.parent_folder}" onclick="UpdateFileBrowser('${data.parent_folder}')">
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
        <tr data-id="${item.id}" onclick="UpdateFileBrowser('${item.pk}')">
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
            <td>Folder</td>
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
        function () { alert('Failure') }
    )

    CURRENT_FOLDER = fid;
}

function GetPersonalVault(uid) {
    
}