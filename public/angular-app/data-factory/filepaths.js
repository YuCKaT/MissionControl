/**
 * Created by konrad.sobon on 2018-08-30.
 */
angular.module('MissionControlApp').factory('FilePathsFactory', FilePathsFactory);

function FilePathsFactory($http){
    return {
        getAll: function (centralPath) {
            return $http.get('/api/v2/filepaths').then(complete).catch(failed);
        },

        addToProject: function (data) {
            return $http.put('/api/v2/filepaths/add', data).then(complete).catch(failed);
        },

        changeFilePath: function (data) {
            return $http.put('/api/v2/filepaths/change', data).then(complete).catch(failed);
        },

        removeFromProject: function (data) {
            return $http.put('/api/v2/filepaths/remove', data).then(complete).catch(failed);
        },

        removeManyFromProject: function (data) {
            return $http.put('/api/v2/filepaths/removemany', data).then(complete).catch(failed);
        },

        addMany: function (data) {
            return $http.post('/api/v2/filepaths/addmany', data).then(complete).catch(failed);
        }
    };

    function complete(response) {
        return response;
    }

    function failed(error) {
        console.log(error.statusText);
        return error;
    }
}